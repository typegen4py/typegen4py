import ast
import os
import re
import sys
import json
import random
import astunparse
from collections import OrderedDict
from copy import deepcopy
from core.func_call_visitor import get_func_calls, get_call_type
import _ast
from util import get_all_alias, tell_type
from ast_factory import ParseVisitor
from ast_factory import *
#from CFG import CFGBuilder
from cfg import CFGBuilder
from import_graph.import_graph import ImportGraph, Tree
from comment_parser import comment_parser
from wheel_inspect import inspect_wheel
import tarfile
from zipfile import ZipFile
from pkg_resources import parse_version

from stub import lookup_typeshed, lookup_typeshed_single, read_stub_types
random.seed(100)

def process_code (code_text):

    def pick_type(type_lst):
        base_type_names = ["Num", "Set", "List", "Tuple", "Dict", "Str", "NameConstant"]
        new_type_lst = []
        type_hint_pairs = []
        l = len(type_lst[0])
        if l == 0:
            # no arguments required
            return []
        type_lst = filter(lambda x: len(x)==l, type_lst)
        for i in range(l):
            i_th = [t[i] for t in type_lst]
            new_type_lst += [None]
            for tmp in i_th:
                if tmp in base_type_names:
                    new_type_lst[-1]= tmp
                    break
            for tmp in i_th:
                if isinstance(tmp, tuple) and tmp[0] == "Call":
                    if new_type_lst[i] is not None:
                        type_hint_pairs += [(tmp[1],new_type_lst[i])]

        return type_hint_pairs

    try:
        # then return value is tuple
        tree = ast.parse(code_text, mode = 'exec')
        visitor = ParseVisitor()
        visitor.visit(tree)
        func_arg_db = {}
        final_func_arg_db = {}
        function_arg_types = get_call_type(tree)
        type_hint_pairs = visitor.type_hint_pairs
        all_call_names = []
        import_nodes = visitor.import_nodes
        import_dict =  get_api_ref_id(import_nodes)
        class2obj = visitor.class_obj

        all_func_names = []

        for pair in function_arg_types:
            name, arg_type = pair
            name_parts = name.split('.')

            name = ".".join(name_parts)
            all_call_names += [name]

            if name in func_arg_db:
                func_arg_db[name] += [arg_type]
            else:
                func_arg_db[name] = [arg_type]
        for func, arg_type in func_arg_db.items():
             type_hint_pairs += pick_type(arg_type)
             #tmp = pick_type(arg_type)
             #print(tmp) 
        return type_hint_pairs, visitor.call_links, all_call_names

        final_info = {
                'call_type_lst': call_type_lst, 
                'class2obj': class2obj,
                'import_dict': import_dict,
                'type_hint_pair': type_hint_pair,
                'source': code_text
                }
        return final_info 
    except (SyntaxError, UnicodeDecodeError):
        return {}, {}, []

def is_done(t_vals):
    return all(x not in ['ID', 'call', 'unknown', 'input', '3call'] for x in t_vals)

def is_valid_call_link(t_vals):
    return all(x not in ['ID', 'call', 'unknown'] for x in t_vals)


def parse_module(m_ast):

    fun_nodes = []
    class_nodes = []
    import_nodes = []

    for node in m_ast.body:
        if isinstance(node, ast.FunctionDef):
            fun_nodes += [node]
        if isinstance(node, ast.ClassDef):
            class_nodes += [node]
    for node in ast.walk(m_ast):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            import_nodes += [node]

    return fun_nodes, class_nodes, import_nodes

def get_return_value(block):
    for stmt in block.statements:
        if isinstance(stmt, ast.Return):
            return stmt.value
    return None

def is_imported_fun(func_name, import_dict):
    name_parts = func_name.split('.')
    if name_parts[0] in import_dict:
        return import_dict[name_parts[0]]
    return None

def extract_info_from_comment(comment):
    base_types = {'int', 'float', 'str', 'bool', 'boolean', 'set', 'list',
            'dict', 'tuple', "true", "false"}
    comment = re.sub(r"\\n", ' ', comment).lower()
    # return/returns
    return_idx = comment.find("return")
    if return_idx <0:
        return None
    tokens = comment.split()
    for token in tokens:
        if token in base_types:
            if token == 'true' or token == 'false':
                return "NC"
            return token
    return None


class AutoTyper:

    def __init__(self, name, entry_point, lib_name=None):
        self.name = name
        self.ep = entry_point
        self.lib_name = lib_name
        
        if self.ep.endswith(".py"):
            self.root_node = Tree(os.path.basename(self.ep))
        else:
            self.root_node = Tree(self.name)
        self.m_graph = None
        self.leaf_stack = []

    # build graph of the directory
    def init(self):
        cwd = os.getcwd() # save current working dir
        working_dir = os.path.dirname(self.ep)
        os.chdir(working_dir)
        self.m_graph = ImportGraph(self.ep, self.root_node)
        self.m_graph.build_dir_tree(self.root_node)
        os.chdir(cwd) # go back cwd

        working_queue = []
        working_queue.append(self.root_node) 
        #print(self.root_node)
        all_nodes = []
        # build leaf stack
        while len(working_queue)>0:
            tmp_node = working_queue.pop(0)
            if tmp_node.name.endswith('.py') == True:
                self.leaf_stack.append(tmp_node)
            working_queue.extend(tmp_node.children)

    def gen_ast(self, source):
        try:
            #tree = ast.parse(source, mode ='exec', type_comments=True)
            tree = ast.parse(source, mode ='exec')
            return tree
        except Exception as e:
            return None

    def process_single_module(self, source):
        node_type_dict = {}
        node_type_comment = {}
        node_type_gt = {}
        stem_from_dict = {}
        type_stem_links = {}
        class2base = {}
        tree = self.gen_ast(source)
        if tree is None:
            return node_type_dict, node_type_gt, type_stem_links, node_type_comment

        split_visitor = SourceSplitVisitor()
        return_visitor = ReturnStmtVisitor()
        # to extract all fun node and class nodes
        split_visitor.visit(tree)
        assign_records = split_visitor.assign_dict
        return_visitor.import_assign_records(assign_records)
        all_methods, all_classes, import_nodes  = parse_module(tree)
        import_dict =  get_api_ref_id(import_nodes)


        for fun_node in all_methods: 
            fun_src = astunparse.unparse(fun_node)
            matches=re.findall(r"\'(.+?)\'", fun_src)
            comment = ''
            if len(matches) >0:
                comment =  matches[0]

            fun_name = fun_node.name
            return_visitor.clear()
            return_visitor.visit(fun_node)
            node_type_comment[fun_name] = comment

            node_type_dict[fun_name] = None
            node_type_gt[fun_name] = None

            if return_visitor.n_returns ==0:
                continue

            r_types = return_visitor.r_types
            node_type_dict[fun_name] = r_types
            stem_from_dict[fun_name] = return_visitor.stem_from
            node_type_gt[fun_name] = fun_node.returns

        for class_node in all_classes:
            #break
            class_visitor = ClassSplitVisitor()
            class_visitor.visit(class_node)
            class_name = class_node.name
            #  what about more than one base class?
            base_class_name = None
            if len(class_node.bases)>0:
                if isinstance(class_node.bases[0], ast.Name):
                    class2base[class_name] = class_node.bases[0].id
            class_assign_records = class_visitor.class_assign_records
            return_visitor.clear_all()
            return_visitor.import_class_assign_records(class_assign_records)
            for fun_node in class_visitor.fun_nodes:
                # classname.funname
                fun_name = "{}.{}".format(class_name, fun_node.name)
                fun_src = astunparse.unparse(fun_node)
                matches=re.findall(r"\'(.+?)\'", fun_src)
                comment = ""
                if len(matches) >0:
                    comment =  matches[0]
                node_type_comment[fun_name] = comment

                return_visitor.clear()
                return_visitor.visit(fun_node)
                node_type_dict[fun_name] = None
                node_type_gt[fun_name] = None
                if return_visitor.n_returns == 0:
                    continue

                r_types = return_visitor.r_types
                node_type_dict[fun_name] = r_types
                stem_from_dict[fun_name] = return_visitor.stem_from
                node_type_gt[fun_name] = fun_node.returns

       # we only look at return stmts that called another function
        for fun_name, stems in stem_from_dict.items():
            #assert node_type_dict[fun_name] is not None
            # keep the order, this is important
            stems = list(dict.fromkeys(stems))
            for from_name in stems:
                # from the same class
                if from_name.find('self.')==0:
                    type_stem_links[fun_name] = ('self',from_name )
                elif from_name.find('super.')==0:
                    class_name = fun_name.split('.')[0]
                    if class_name in class2base:
                        base_name = class2base[class_name]
                        if base_name in import_dict:
                            type_stem_links[fun_name] = (import_dict[base_name], base_name+from_name.lstrip('super') ) 
                        else:
                            type_stem_links[fun_name] = ('base', base_name+ from_name.lstrip('super') )
                    else:
                        # can be from other libraries as well
                        pass
                elif from_name in node_type_dict:
                    type_stem_links[fun_name] = ('local',from_name )
                else:
                    import_path = is_imported_fun(from_name, import_dict)
                    if import_path is not None:
                        type_stem_links[fun_name] = (import_path, from_name )
                   # debugging
        return node_type_dict, node_type_gt, type_stem_links, node_type_comment

    def step2(self):

        for node in self.leaf_stack:
            node_type_dict,node_type_gt,  type_stem_links, node_type_comment = self.process_single_module(node.source)
            node.node_type_dict = node_type_dict
            node.node_type_gt = node_type_gt
            node.call_links = type_stem_links

    def rename_from_name(self, from_where, from_name, fun_name):
        if from_where == 'self':
            class_name = fun_name.split('.')[0]
            from_name = class_name + "."+ ".".join(from_name.split('.')[1:])
            return from_name
        elif from_where == 'local' or from_where == 'base':
            return from_name

    def step3(self):
        for node in self.leaf_stack:
            for fun_name, (from_where, from_name) in node.call_links.items():
                # same module
                if node.node_type_dict[fun_name] is None:
                    continue 

                if from_where in ['self', 'local', 'base']: 
                    from_name = self.rename_from_name(from_where, from_name, fun_name) 
                    if from_name in node.node_type_dict and node.node_type_dict[from_name] is not None:
                        t_vals_tmp = node.node_type_dict[from_name]
                        if is_valid_call_link(t_vals_tmp):
                            node.node_type_dict[fun_name] += t_vals_tmp
                # might be from other modules
                else:
                    visit_path = from_where.split('.')
                    if len(visit_path) == 1 and visit_path[0] == self.m_graph.root.name:
                        dst_node = self.m_graph.root
                    else:
                        dst_node = self.m_graph.go_to_that_node(node, from_where.split('.')[0:-1])

                    if dst_node is not None: 
                        if hasattr(dst_node, "node_type_dict") and dst_node.node_type_dict is not None: 
                            if from_name in dst_node.node_type_dict and dst_node.node_type_dict[from_name] is not None:
                                t_vals_tmp = dst_node.node_type_dict[from_name]
                                if is_valid_call_link(t_vals_tmp):
                                    node.node_type_dict[fun_name] += t_vals_tmp
                                #node.node_type_dict[fun_name] +=  dst_node.node_type_dict[from_name]
                    else:
                        # this is a library call 3call be propagated to other affected calls
                        node.node_type_dict[fun_name] += ["3call"]

    def find_class_by_attr(self, module_records, attrs):
        # this is a treshold

        if len(attrs) <5:
            return None
        class_names = [item.split('.')[0] for item in module_records  if len(item.split('.'))==2]
        class_names = list(set(class_names))
        for c_name in class_names:
            if all([(c_name+'.'+x) in module_records for x in attrs]):
                return c_name
            
        return None


    def step4(self):
        for node in self.leaf_stack:
            type_hint_pairs, client_call_link, all_call_names = process_code(node.source)
            for pair in type_hint_pairs:
                if pair is None:
                    continue
                fun_name, t_val = pair
                if t_val in ['call', 'input']:
                    continue
                #print(fun_name, node.node_type_dict[fun_name])
                # type hints are known 
                if fun_name in node.node_type_dict and node.node_type_dict[fun_name] is not None:
                    if "input" in node.node_type_dict[fun_name]:
                        node.node_type_dict[fun_name] = [t_val]
                    if "3call" in node.node_type_dict[fun_name]:
                        node.node_type_dict[fun_name] = [t_val]
                    if "unknown" in node.node_type_dict[fun_name]:
                        node.node_type_dict[fun_name] = [t_val]
                    else:
                        node.node_type_dict[fun_name] += [t_val]

            for call_pair in client_call_link:
                if call_pair is None:
                    continue
                fun1, fun2 = call_pair
                # in the same module
                if fun1 in node.node_type_dict and fun2 in node.node_type_dict:
                    # they share with each other 
                    fun1_t_val = node.node_type_dict[fun1]
                    fun2_t_val = node.node_type_dict[fun2]
                    if is_done(fun1_t_val) and (not is_done(fun2_t_val)):
                        node.node_type_dict[fun2] = fun1_t_val
                    if is_done(fun2_t_val) and (not is_done(fun1_t_val)):
                        node.node_type_dict[fun1] = fun2_t_val
            fun_access_attr_records = {}
            for call_name in all_call_names:
                call_name_segs = call_name.split('.')
                if len(call_name_segs) <2:
                    continue
                if call_name_segs[0] not in node.node_type_dict:
                    continue

                if call_name_segs[0] not in fun_access_attr_records:
                    fun_access_attr_records[call_name_segs[0]] = [call_name_segs[1]]
                else:
                    fun_access_attr_records[call_name_segs[0]] += [call_name_segs[1]] 

            for fun_name, access_attrs in fun_access_attr_records.items():
                access_attrs = list(set(access_attrs))
                class_infered =  self.find_class_by_attr(list(node.node_type_dict.keys()), access_attrs )
                if class_infered is not None:
                    node.node_type_dict[fun_name] = [class_infered]

    def stat(self, l_name = ""):
        n_total = 0
        n_valid = 0
        n_clear = 0
        n_input = 0
        n_3call = 0

        for node in self.leaf_stack:
            n_total += len(node.node_type_dict)
            for k, t_vals in node.node_type_dict.items():
                if t_vals is None:
                    continue
                n_valid += 1
                if len(t_vals)== 0:
                    continue
                if is_done(t_vals):
                    n_clear += 1
                elif "3call" in t_vals or '3call' in t_vals:
                    n_3call += 1
                elif "input" in t_vals:
                    n_input += 1
        n_selected = n_valid-n_input-n_3call


        print(",".join([l_name, str(n_total), str(n_selected), str(n_clear)]) , n_clear/n_selected)
        print(n_input, n_3call)
    def print_all(self):
        for node in self.leaf_stack:
            for k, t_vals in node.node_type_dict.items():
                if t_vals is None:
                    continue
                if len(t_vals)== 0:
                    continue
                if is_done(t_vals):
                    print(node.prefix, ",", k, set(t_vals))


    def eval(self):
        n_annot = 0
        n_correct = 0
        n_input = 0
        n_external = 0
        n_zero =0
        n_fail = 0
        for node in self.leaf_stack:
            for k,v in node.node_type_gt.items():
                if v is None:
                    continue
                if node.node_type_dict[k] is None:
                    continue

                gt = format_type_annot(v)
                if gt in ["t.Optional", "Optional"] and hasattr(v, "slice"):
                    gt = format_type_annot(v.slice)
                       # gt = format_type_annot(v.slice)
                if gt in ["t.Any", "Any", "None", None]:
                    continue

                pred = node.node_type_dict[k]

                if "3call" in pred or '3call' in pred :
                    n_external += 1
                    continue
                if  "input" in pred or 'input' in pred:
                    n_input += 1
                    continue

                n_annot += 1
                fun_name = k

                if len(pred) == 0:
                    n_fail += 1
                    continue

                if check_with_gt(fun_name, gt,pred):
                    n_correct += 1
                else:
                   # print( gt, ':', pred)
                    pass
        print(",".join([str(n_annot),str(n_fail), str(n_correct), str(n_correct/n_annot)]))

    def print_known(self):
        func_all = set()
        n_missing = 0
        n_known = 0
        for leaf_node in self.leaf_stack:
            for fun_name, t_vals in leaf_node.node_type_dict.items():
                
                if t_vals is None:
                    continue
                #print(fun_name, t_vals)
                if len(t_vals)== 0:
                    continue
                if is_done(t_vals):
                    #print(leaf_node.prefix+"."+fun_name, t_vals)
                    n_known += 1
                    print(leaf_node.prefix, fun_name, set(t_vals))
        #print(n_known)
 
    def query_typeshed(self, ep): 
        base_dir = "./typeshed/stubs/requests"
        ##base_dir = "./typeshed/stubs/Jinja2"
        #base_dir = "./typeshed/stubs/Flask"
        typeshed_func = set()
        n_missing = 0
        n_fun_typed = 0
        n_all, n_modules = lookup_typeshed(base_dir, ep)
        for leaf_node in self.leaf_stack:
            leaf_path_segments = leaf_node.prefix.split(".")
            #pyi_file = leaf_path_segments[-1].rstrip(".py") +".pyi"
            #pyi_file = leaf_node.name+ 'i'
            #pyi_file_path = base_dir+"/"+ "/".join(leaf_path_segments[1:-1])+"/"+pyi_file
            pyi_file_path = base_dir+"/"+ "/".join(leaf_path_segments[1:-1]) + ".pyi"
            #print(leaf_node.name)
            #print(pyi_file_path)
            if os.path.exists(pyi_file_path):
                #n_returns, fun_name_lst  = lookup_typeshed_single(pyi_file_path)
                shed_type_dict = read_stub_types(open(pyi_file_path).read())
                #n_fun_typed += n_returns
                for fun_name, pred_type in leaf_node.node_type_dict.items():
                    if fun_name in shed_type_dict and shed_type_dict[fun_name] is not None:
                        shed_type_str = format_type_annot(shed_type_dict[fun_name])
                        if check_with_gt(fun_name, format_type_annot(shed_type_dict[fun_name]), pred_type):
                            print("Yes")
                        else:
                            print("No")
                    else:
                        print("Not found")
         #           print(full_name)
            else:
                n_missing += 1 
                #print(pyi_file_path, leaf_node.prefix)
            continue
            #for fun_name, r_vals in leaf_node.node_type_dict.items():
            #    if t_vals is None:
            #        continue
            #    if len(t_vals)== 0:
            #        continue
            #    if is_done(t_vals):
            #        pass 
        #print(self.lib_name, ",", len(self.leaf_stack), ",",
        #        len(self.leaf_stack)- n_missing)
        print(n_fun_typed)
        print(n_missing)

    def cmp_pytype_shed(self): 
        shed_base_dir = "./typeshed/stubs/requests"
        pytype_base_dir = "pytype-res/pyi/"
        #base_dir = "./typeshed/stubs/Jinja2"
        #base_dir = "./typeshed/stubs/Flask"
        #base_dir = "pytype-res/pyi/flask"
        #base_dir = "pytype-res/pyi/jinja2"
        typeshed_func = set()
        n_missing = 0
        n_fun_typed = 0
        for leaf_node in self.leaf_stack:
            leaf_path_segments = leaf_node.prefix.split(".")
            shed_stub_path = shed_base_dir+"/"+ "/".join(leaf_path_segments[1:-1]) + ".pyi"
            pytype_stub_path = pytype_base_dir+"/"+ "/".join(leaf_path_segments[1:-1]) + ".pyi"
            #print(shed_stub_path)
            #print(pytype_stub_path)
            if os.path.exists(shed_stub_path) and os.path.exists(pytype_stub_path) :
                #n_returns, fun_name_lst  = lookup_typeshed_single(pyi_file_path)
                shed_type_dict = read_stub_types(open(shed_stub_path).read())
                pytype_type_dict = read_stub_types(open(pytype_stub_path).read())
                #n_fun_typed += n_returns
                for fun_name, shed_type in shed_type_dict.items():
                    if fun_name in pytype_type_dict:
                        if isinstance(shed_type, ast.NameConstant) and shed_type.value is None:
                            continue           
                        if shed_type is None:
                            continue
                        #print("testing")
                        shed_type_str = format_type_annot(shed_type)
                        pytype_type_str = format_type_annot(pytype_type_dict[fun_name])
                        #if shed_type_str  == "None":
                        #    continue
                        #if shed_type_str is None:
                        #    continue
                    #    if check_with_gt(shed_type_str, )
                        if pytype_type_str != shed_type_str and shed_type_str not in pytype_type_str:
                            print(pytype_type_str, fun_name, "No--", "pytype:", pytype_type_str, "shed:", shed_type_str)
                        #else:
                        #    print("Yes")
            else:
                n_missing += 1 
                #print(pyi_file_path, leaf_node.prefix)
            continue
        print(n_fun_typed)
        print(n_missing)

    def query_pytype(self, ep): 
        #base_dir = "./typeshed/stubs/requests"
        #base_dir = "./pytype/pyi/"
        base_dir = "pytype-res/pyi"
        #base_dir = "./typeshed/stubs/Jinja2"
        #base_dir = "./typeshed/stubs/Flask"
        #base_dir = "pytype-res/pyi/flask"
        #base_dir = "pytype-res/pyi/jinja2"
        typeshed_func = set()
        n_missing = 0
        n_fun_typed = 0
        n_common_total = 0
        n_same = 0
        n_any = 0
        n_pytype_only = 0
        n_not_same = 0
        for leaf_node in self.leaf_stack:
            leaf_path_segments = leaf_node.prefix.split(".")
            pyi_file_path = base_dir+"/"+ "/".join(leaf_path_segments[0:-1]) + ".pyi"
            #print(leaf_node.name)
            #print(pyi_file_path)
            if os.path.exists(pyi_file_path):
                #n_returns, fun_name_lst  = lookup_typeshed_single(pyi_file_path)
                shed_type_dict = read_stub_types(open(pyi_file_path).read())
                #n_fun_typed += n_returns
                for fun_name, shed_type in shed_type_dict.items():
                    if fun_name in leaf_node.node_type_dict:
                        pred_type = leaf_node.node_type_dict[fun_name]
                        if shed_type is None:
                            continue
                        shed_type_str = format_type_annot(shed_type)
                        if shed_type_str  == "None":
                            continue
                        if shed_type_str is None:
                            continue
                        if pred_type is None:
                            continue
                        if not is_done(pred_type) or len(pred_type) == 0:
                            if shed_type_str !="Any":
                                n_pytype_only  += 1
                            continue 
                        #if  shed_type_str not in pred_type:
                        #    print(fun_name, pyi_file_path, shed_type_str, pred_type)
                        if pred_type is None:
                        #    print(fun_name, pyi_file_path, shed_type_str, pred_type)
                            continue
                        if "Any" == shed_type_str:
                                n_any += 1

                
                        #if  shed_type_str  in pred_type or shed_type_str.lower() in pred_type:
                        # both tools give results when it reaches here
                        if shed_type_str != "Any":
                            n_common_total += 1
                        else:
                            continue
                        if check_with_gt(fun_name, shed_type_str, pred_type):
                            n_same += 1    
                        else:
                            n_not_same += 1
                            print(fun_name, pyi_file_path, shed_type_str, pred_type)
                    #else:
                    #    shed_type_str = format_type_annot(shed_type)
                        
                    #    if shed_type_str is not None and shed_type_str != "Any":
                    #        n_pytype += 1
                    #    print(pyi_file_path, fun_name, ast.dump(shed_type))
                        #print(leaf_node.node_type_dict.keys())
            else:
                n_missing += 1 
                #print("testing")
                #print(pyi_file_path, leaf_node.prefix)
            #continue
        print("Pytype only: {},   identical: {}, non-identical: {}, common {}".format(n_pytype_only,n_same, n_not_same, n_common_total))
        #print("Common{}/{}, {}".format())
        #print(n_pytype)
        #print("comparsion results:", "common", n_common_total, "same", n_same, "any", n_any, "other", n_common_total-n_any-n_same)
        

def get_source_folder(base_dir, folders):
    if "_pytest" in folders:
        return "_pytest"
    for foder_name in folders:
        tmp_path = os.path.join(base_dir, foder_name)
        if foder_name[0] in ["_"]:
            return foder_name
        if foder_name.find(".data") >=0:
            continue
        if foder_name.find(".mypy") >=0:
            continue
        if foder_name.find("out") >=0:
            continue
        if os.path.isdir(tmp_path) and foder_name.find(".dist-info") == -1:
            return foder_name
    for foder_name in folders:
        if foder_name.endswith(".py") and (not foder_name.startswith("test")):
            return foder_name
    return None


def process_single_lib(data_dir):
    if not os.path.exists(data_dir):
        print(data_dir)
        print('Wrong!!')
        return
    ep = get_source_folder(data_dir, os.listdir(data_dir)) 
    if ep is None:
        return 
    if ep.endswith(".py"):
        ep = os.path.join(data_dir, ep)
        m_name = ep.rstrip(".py")
    else:
        m_name = ep
        ep = os.path.join(data_dir, m_name)

    auto_typer = AutoTyper(m_name, ep, lib_name=m_name) 
    auto_typer.init()
    auto_typer.step2()
    #auto_typer.stat(l_name=m_name)

    auto_typer.step3()
    auto_typer.step3()
    auto_typer.step4()
    #auto_typer.query_typeshed(ep)
    auto_typer.query_pytype(ep)
    #auto_typer.cmp_pytype_shed()
    #auto_typer.stat(l_name=m_name)
    #auto_typer.eval()


def format_type_annot(annot):
       
    
    if isinstance(annot, ast.Tuple):
        #print(ast.dump(annot))
        return [format_type_annot(elt) for elt in annot.elts]
    if isinstance(annot, ast.Name):
        return annot.id
    if isinstance(annot, ast.Str):
        return annot.s
    
    elif isinstance(annot, ast.Constant):
        return annot.value
    elif isinstance(annot, ast.Subscript):
        if isinstance(annot.value, ast.Name) and annot.value.id in ["Optional", "t.Optional"]:
            return  format_type_annot(annot.slice)
        if isinstance(annot.value, ast.Name) and annot.value.id in  ["Union", "t.Union"]:
            
            return  format_type_annot(annot.slice)
        
        if isinstance(annot.value, ast.Name) and annot.value.id == "Literal":
            
           return  format_type_annot(annot.slice)
    
    

         
        return format_type_annot(annot.value) 
    elif isinstance(annot, ast.Attribute):
        attr_name = get_attr_name(annot)
        return attr_name
    elif isinstance(annot, ast.Index):
        return format_type_annot(annot.value)
    elif isinstance(annot, ast.NameConstant):
        return annot.value
    else:
        #return ast.dump(annot)
        #print(ast.dump(annot), 'testing')
        return ""
def match(pattern, pred):
    for value in pred:
        if pattern in value:
            return True
    return False

def check_with_gt(fun_name, gt, pred):

    if isinstance(gt, list):
        return all([check_with_gt(fun_name, elt, pred) for elt in gt])


    if gt.split("[")[0] in pred:
        return True
    if gt is None and pred is None:
        return True
    if gt is None:
        if ("None" in pred or "empty" in pred):
            return True
        else:
            return False
    #if gt is None:
    #    gt = "None"

    if gt is not None and pred is None:
        return False

    if gt in pred or gt.lower() in pred:
       return True

    if gt.split(".")[-1] in pred:
        return True
    if gt == "NoReturn" and "empty" in pred:
        return True
    if "lambda" in pred:
        return True
    elif gt is None:
        if ("NC" in pred or "empty" in pred):
            return True
    elif gt == fun_name.split('.')[0] and "self" in pred:
        return True
    elif gt == 'bool' and "NC" in pred:
        return True
    elif gt in  ["t.Iterator", "Iterator"] and ("generator" in pred or "iterator" in
            pred or "list" in pred):
        return True
    elif gt in ["t.Iterable", "Iterable"] and ("list" in pred or "set" in pred or
            match("Iterator", pred)):
        return True
    elif gt == "Sequence" and "list" in pred:
        return True
    elif gt == 'Iterable' and ("generator" in pred or "iterator" in
            pred):
        return True
    elif gt == 't.Tuple' and "tuple" in pred:
        return True
    elif gt == "t.List" and "list" in pred:
        return True
    elif gt in ["int", "float", "num"] and "num" in pred:
        return True
    elif gt.startswith("t.") and (gt[2:]in pred or gt[2:].lower() in
    pred):
        return True
    elif gt == "t.Mapping" and ("CallbackDict" in pred or "dict" in
            pred):
        return True
    elif gt == "t.BinaryIO" and "io.BytesIO" in pred or "BytesIO" in pred:
        return True
    elif gt == "t.Callable" and "Callable" in pred:
        return True
    elif  "self" in pred:
        return True
    elif gt == "List" and "list" in pred:
        return True
    elif gt == "Tuple" and "tuple" in pred:
        return True
    elif gt == "ast.expr":
        return True
    elif gt in ["Dict", "t.Dict"] and ("dict" in pred or match("Dict", pred)):
        return True
    elif gt[0:2]=="_T" and gt[2:] in pred:
        return True
    elif gt[0:9] == "builtins." and gt[9:] in pred:
        return True
    else:
        #print(gt, pred)
        return False

def check_three_GT_libs():
    top_10 = open("gt.txt").readlines()
    all_lib_names = [x.strip() for x in top_10]
    for lib_name in all_lib_names:
        lib_name = lib_name.strip()
        if lib_name in top_10:
            continue
        data_dir  = os.path.join("top-10", lib_name, "tmp")
        if not os.path.exists(data_dir):
            print('Wrong!!')
            continue
        ep = get_source_folder(data_dir, os.listdir(data_dir)) 
        if ep is None:
            continue
        if ep.endswith(".py"):
            ep = os.path.join(data_dir, ep)
            m_name = ep.rstrip(".py")
        else:
            m_name = ep
            ep = os.path.join(data_dir, m_name)

        auto_typer = AutoTyper(m_name, ep, lib_name=lib_name) 
        auto_typer.init()
        auto_typer.step2()

        # multiple times of step3 to do it iteratively
        auto_typer.step3()
        auto_typer.step3()
        auto_typer.step4()
        auto_typer.eval()

def typeshed_stat():
    all_lib_names = open("typeshed-libs.txt").readlines()
    for lib_name in all_lib_names:
        lib_name = lib_name.strip()
        n_all, m_modules = lookup_typeshed("typeshed/stubs/"+lib_name)
        #print("# functions: {}, # modules: {}".format(n_all, m_modules))
        print(n_all, ",", m_modules)

def main():
    op = sys.argv[1]
    if op == "eval":
        check_three_GT_libs()
    elif op == "gen":
        data_dir = sys.argv[2]
        process_single_lib(data_dir)
    elif op == "bench":
        case_name = sys.argv[2]
        benchmark_test(case_name)
    elif op == "typeshed":
        typeshed_stat()

def benchmark_test(case_name):
    lib_name = case_name
    m_name = case_name
    ep  = "benchmark/"+case_name
    auto_typer  =  AutoTyper("case_name", "case_name")
    auto_typer = AutoTyper(m_name, ep, lib_name=lib_name)
    auto_typer.init()
    auto_typer.step2()
    auto_typer.step4()
    auto_typer.step3()
    auto_typer.print_known()


if __name__ == '__main__':
    #check_three_GT_libs()
    main()
