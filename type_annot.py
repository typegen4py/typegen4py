import ast
import os
import re
import sys
import json
import random
import astunparse
from copy import deepcopy
#from core.source_visitor import SourceVisitor

from stub import lookup_typeshed, lookup_typeshed_single, read_stub_types
from core.func_call_visitor import get_func_calls, get_call_type
import _ast
from util import get_all_alias, tell_type
from ast_factory import ParseVisitor
from ast_factory import *
#import pygraphviz as pgv
from import_graph.import_graph import ImportGraph, Tree
from comment_parser import comment_parser
from wheel_inspect import inspect_wheel
import tarfile
from zipfile import ZipFile
from pkg_resources import parse_version

random.seed(100)


def get_return_node(node):
    visitor = ReturnStmtVisitor()
    visitor.visit(node)
    return visitor.ast_nodes

def get_api_ref_id(import_nodes):
    id2fullname  = {}  # key is the imported module while the value is the prefix
    for node in import_nodes:
        if isinstance(node, ast.Import):
            items = [nn.__dict__ for nn in node.names]
            for d in items:
                if d['asname'] is None:  # alias name not found, use its imported name
                    id2fullname[d['name']] = d['name']
                else:
                    id2fullname[d['asname']] = d['name'] # otherwise , use alias name
        if isinstance(node, ast.ImportFrom) and node.module is not None:
            # for import from statements
            # module names are the head of a API name
            items = [nn.__dict__ for nn in node.names]
            for d in items:
                if d['asname'] is None: # alias name not found
                    id2fullname[d['name']] = node.module+'.'+d['name']
                else:
                    id2fullname[d['asname']] = node.module+'.'+d['name']
    return id2fullname


def process_single_module(source, fn, working_dir):

    tree = ast.parse(source, mode ='exec', type_comments=True)

    split_visitor = SourceSplitVisitor()
    return_visitor = ReturnStmtVisitor()

    # to extract all fun node and class nodes
    split_visitor.visit(tree)
    assign_records = split_visitor.assign_dict
    return_visitor.import_assign_records(assign_records)
    # get all methods and class nodes
    #all_methods, all_classes, import_nodes  = parse_module(tree)
    all_classes = []
    all_methods = []
    for stmt in tree.body:
        if isinstance(stmt, ast.FunctionDef):
            all_methods += [stmt]
        if isinstance(stmt, ast.ClassDef):
            all_classes  += [stmt]

    #import_dict =  get_api_ref_id(import_nodes)
    # to store method: [return types]
    node_type_comment = {}

    name_set = set()
    node_type_form = {}
    stub_node_dict = None
    stub_file_path = working_dir + '/' + fn+'i'
    #print(stub_file_path, fn)
    if os.path.exists(stub_file_path):
       
        stub_node_dict = read_stub_types(open(stub_file_path).read())
     
            
    

    for fun_node in all_methods:
        #print(ast.dump(fun_node))
        return_visitor.clear()
        return_visitor.visit(fun_node)

        fun_name = fun_node.name
        node_type_form[fun_name] = None

        if return_visitor.n_returns == 0:
            continue

        fun_src = astunparse.unparse(fun_node)
        matches=re.findall(r"\'(.+?)\'", fun_src)
        comment = ''

        if len(matches) >0:
            comment =  matches[0]
        fun_name = fun_node.name
     
        #--------------------------------
        node_type_form[fun_name] = {"type_annot": False, "type_comment":False, "comment":False, "stub":False}

        if hasattr(fun_node, "returns") and fun_node.returns is not None: 
            node_type_form[fun_name]["type_annot"] = True

        if hasattr(fun_node, "type_comment") and fun_node.type_comment is not None:
            node_type_form[fun_name]["type_comment"] = True
        
               
        if stub_node_dict is not None and fun_name in stub_node_dict:
            node_type_form[fun_name]["stub"] = True
        
        

        #--------------------------------
        fun_src = astunparse.unparse(fun_node)
        matches=re.findall(r"\'(.+?)\'", fun_src)
        comment = ""
        if len(matches) >0:
            comment =  matches[0]
        node_type_comment[fun_name] = comment

    for class_node in all_classes:
        class_visitor = ClassSplitVisitor()
        class_visitor.visit(class_node)
        class_name = class_node.name
        c_fun_nodes = []
        for stmt in class_node.body:
            if isinstance(stmt, ast.FunctionDef):
                c_fun_nodes += [stmt]

        #for fun_node in class_visitor.fun_nodes:
        for fun_node in c_fun_nodes:
            # classname.funname
            fun_name = "{}.{}".format(class_name, fun_node.name)
            return_visitor.clear()
            return_visitor.visit(fun_node)
            node_type_form[fun_name] = None

            if return_visitor.n_returns == 0:
                continue
            #--------------------------------
            node_type_form[fun_name] = {"type_annot": False, "type_comment":False, "comment":False, "stub":False}
            if hasattr(fun_node, "returns") and fun_node.returns is not None: 
                node_type_form[fun_name]["type_annot"] = True

            if hasattr(fun_node, "type_comment") and fun_node.type_comment is not None:
                node_type_form[fun_name]["type_comment"] = True
            
            if stub_node_dict is not None and fun_name in stub_node_dict:
                node_type_form[fun_name]["stub"] = True

            #--------------------------------

            fun_src = astunparse.unparse(fun_node)
            matches=re.findall(r"\'(.+?)\'", fun_src)
            comment = ""
            if len(matches) >0:
                comment =  matches[0]
            node_type_comment[fun_name] = comment


    for fun_name, comment in node_type_comment.items():
        if node_type_form[fun_name] is None:
            continue
        comment_type = extract_info_from_comment(comment)
        if comment_type is not None:
            node_type_form[fun_name]["comment"] = True 

    return node_type_form

def is_imported_fun(func_name, import_dict):
    name_parts = func_name.split('.')
    if name_parts[0] in import_dict:
        return import_dict[name_parts[0]]
    return None

def extract_info_from_comment(comment):
    base_types = {'int', 'float', 'str', "string", 'bool', 'boolean', 'set', 'list',
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
            if token == 'string':
                return "str"
            return token
    return None

def main():
    base_dir = '../lib-type/scalpel/pre-study/'
    #base_dir = 'top-10/'
    all_lib = open(base_dir+'res.txt').readlines()
    top_10 = [
       
            "requests",
            "six",
            "Flask",
            "Django",
            "Jinja2",
            "Numpy",
            "pytz",
            "MarkupSafe",
            "Werkzeug",
            "pytest",
          #  "_pytest"
            ]
    top_15 = [
        "psycopg2",
        "wsgiref",
        "wheel",
        "docutils",
        "boto", 
        "simplejson",
        "scikit-learn", 
        "cffi", 
        "cryptography",
        "Flask-WTF", 
        "httplib2", 
        "pycrypto", 
        "future", 
        "South", 
        "blinker" 
    ]
    #for lib_name in top_10:
    for lib_name in all_lib[90:]:
    #for lib_name in top_15:
        
        try:
            lib_name = lib_name.strip()
            
            version = os.listdir(os.path.join(base_dir, lib_name))
            whl_path = os.path.join(base_dir, lib_name, version[0])
            #whl_path = os.path.join(base_dir, lib_name)
            eps =  process_wheel(whl_path, lib_name)
            for ep in eps:
                process_lib_single(ep, lib_name)
        except Exception as e:
           print(lib_name, str(e))
    return 0

def search_targets(root_dir, targets):
     entry_points = []
     for root, dirs, files in os.walk(root_dir):
         n_found = 0
         for t in targets:
             if t in dirs :
                entry_points.append(os.path.join(root, t))
                n_found += 1
             elif t+'.py' in files:
                 entry_points.append(os.path.join(root, t+'.py'))
                 n_found += 1
         if n_found == len(targets):
             return entry_points
     return None

def process_wheel(path, l_name):
    # there will be multiple wheel files
    res = []
    all_file_names = os.listdir(path)
    whl_final = ''
    max_py_ver = ''
    for fn in all_file_names:
        if fn.endswith('.whl') and (fn.find('linux')>=0 or fn.find('any')>=0):  # this is a wheel
            whl_path = os.path.join(path, fn)
            try:
                output = inspect_wheel(whl_path)
                if output['pyver'][-1]> max_py_ver:  # -1 means the last one. Use the biggest version number
                    max_py_ver = output['pyver'][-1]
                    whl_final = fn
            except Exception as e:
                print("failed to handle {}".format(whl_path))
                print(e)
    if whl_final != '':
        whl_path = os.path.join(path, whl_final)
        output = inspect_wheel(whl_path)
        #print(output.keys())
        if 'top_level' not in output['dist_info']:
            top_levels = [l_name]
        else:
            top_levels = output['dist_info']['top_level']

        with ZipFile(whl_path, 'r') as zipObj:
           # Extract all the contents of zip file in current directory
           source_dir = os.path.join(path, 'tmp')
           if not os.path.exists(source_dir):
               zipObj.extractall(source_dir)
        entry_points = search_targets(source_dir, top_levels)
        return entry_points
    return None

#def process_lib_single(lib_name):
def process_lib_single(ep, lib_name):
    #fn = '/mnt/fit-Knowledgezoo/sklearn-notebooks/2020-scikit-learn-tutorial/notebooks/linear_models.ipynb'
   # fn =  'tests/sklearn/cluster/_kmeans.py'
   # fn = 'tests/sklearn/cluster/_dbscan.py'
   # fn = 'tests/sklearn/cluster/_affinity_propagation.py'
   # fn = 'tests/sklearn/cluster/_mean_shift.py'
    #lib_name = sys.argv[1]
    #ep = 'top-10/'+ lib_name
    root_name = os.path.basename(ep)
    root_node = Tree(root_name)
    # build import graph
 
    cwd = os.getcwd() # save current working dir
    working_dir = os.path.dirname(ep)
    os.chdir(working_dir)
    m_graph = ImportGraph(ep, root_node)
    m_graph.build_dir_tree(root_node)

    os.chdir(cwd) # go back cwd

    leaf_stack = []
    working_queue = []
    working_queue.append(root_node)
    all_nodes = []

    N_all = 0
    N_non_zero = 0
    N_clear = 0

    while len(working_queue)>0:
        tmp_node = working_queue.pop(0)
        if tmp_node.name.endswith('.py') == True:
            leaf_stack.append(tmp_node)
        working_queue.extend(tmp_node.children)

    # visit all elements from the stack 
    n_total  = 0
    n_returns = 0
    n_comment = 0
    n_type_comment = 0
    n_type_annot = 0 
    n_stub = 0
    n_at_least = 0
    for node in leaf_stack:
        
        src_path_segs = node.prefix.split(".")
        src_path = "/".join(src_path_segs[0:-1])+"."+src_path_segs[-1] 
        #rint(src_path)
        node_type_form =  process_single_module(node.source, src_path, working_dir)
        n_total += len(node_type_form)
        for fun_name, type_form in  node_type_form.items():
            if type_form is not None:
                bo = False
                n_returns += 1
                if type_form['comment']:
                    n_comment += 1
                    bo = True
                if type_form['type_comment']:
                    n_type_comment += 1
                    bo = True
                    #print(fun_name, node)
                if type_form['type_annot']:
                    n_type_annot += 1
                    bo = True
                if type_form['stub']:
                    n_stub += 1
                    bo = True
                if bo:
                    n_at_least += 1

    #print("N_total", n_total)
    #print("N_returns", n_returns)
 
    #print(n_comment, n_type_comment, n_type_annot)
    row = [lib_name, str(n_total), str(n_returns), str(n_comment), str(n_type_comment), str(n_type_annot), str(n_stub), str(n_at_least)]
    print(",".join(row))

    return 0



def test():
    fn = sys.argv[1]
    source = open(fn).read()
    tree = ast.parse(source, mode ='exec', type_comments=True)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            print(node.name, node.returns)
            print(ast.dump(node))
            break

    #node_type_form = process_single_module(source)
    #for k, v in node_type_form.items():
    #    print(k, v)

if __name__ == '__main__':
    main()
#    run_scripts()
#    test()
#    run_single_notebook()
#    data_analyse()

