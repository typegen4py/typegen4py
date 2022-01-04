import ast
import re
import os
from core.func_call_visitor import get_func_calls

def get_path_by_extension(root_dir, flag='.py'):
    paths = []
    for root, dirs, files in os.walk(root_dir):
        files = [f for f in files if not f[0] == '.']  # skip hidden files such as git files
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for f in files:
            if f.endswith(flag):
                paths.append(os.path.join(root, f))
    return paths

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

def is_camel_case(s):
    pattern = '([A-Z][a-z]*)+'
    if(re.search(pattern,s)):
        return True
    return False
#
def get_all_alias(alias_pair, name):
    to_do = [name]
    res = []
    while len(to_do) >0:
        name = to_do.pop()

        for pair in alias_pair:
            if pair[0] == name:
                to_do.append(pair[1])
                res += [pair[1]]
    return res

def process_binop():
    return None
def tell_type(node):
    # does not return anything
    if node is None:
        
        return "NC"
    elif isinstance(node, str) and node[0:3] == "org":
        return node[4:]
    elif isinstance(node, ast.BoolOp):
        return "bool"
    #  eq not eq  lt  lte  gt  gte 
    elif isinstance(node, ast.cmpop):
        return "bool"
    elif isinstance(node, ast.Compare):
        return "bool"
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return "bool"
    elif isinstance(node, ast.BinOp):
        
        if isinstance(node.op, (ast.Div, ast.Mult)):
            return "float"
        elif isinstance(node.op, ast.Mod) and isinstance(node.left, ast.Constant) and isinstance(node.left, ast.Str):
            # '(step %d of %d) Processing %s' % (idx, total, name)
            return "str"
        elif isinstance(node.op, ast.Mod) and isinstance(node.left, ast.Name)  and isinstance(node.right, ast.Dict):
            return "str"
        elif isinstance(node.op, ast.Add):
            if isinstance(node.left, (ast.Constant, ast.Num, ast.List, ast.ListComp,
                ast.Set, ast.SetComp, ast.Dict, ast.DictComp)): 
                return tell_type(node.left)

            if isinstance(node.right, (ast.Constant,ast.Num, ast.List, ast.ListComp,
                ast.Set, ast.SetComp, ast.Dict, ast.DictComp)):
                return tell_type(node.right) 
        
        left_type = tell_type(node.left)
        if left_type is not None and left_type not in ["unknown", "ID", "attr"]:
            return left_type
        
        right_type = tell_type(node.right)
        if right_type is not None and right_type not in ["unknown", "ID", "attr"]:
            return right_type
        
    if isinstance(node, ast.Name):
        if node.id == 'self':
            return "self"
        return 'ID'
    if isinstance(node, ast.Num):
        if isinstance(node.n, int):
            return "int"
        elif isinstance(node.n, float):
            return "float" 
        return "num"
    elif isinstance(node, ast.List):
        return "list"
    #elif isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
    elif isinstance(node, ast.Subscript):
        return "subscript"
    elif isinstance(node, ast.Tuple):
        return "tuple"
    elif isinstance(node, ast.Dict):
        return "dict"
    elif isinstance(node, ast.Set):
        return "set"
    elif isinstance(node, ast.SetComp):
        return "set"
    elif isinstance(node, ast.Str):
        return "str"
    elif isinstance(node, ast.JoinedStr):
        return "str"
    elif isinstance(node, ast.NameConstant):
        if isinstance(node.value, bool):
            return "bool"
        
        return "NC"
    elif isinstance(node, ast.Constant):
        ##################
        ############## 
        return tell_type(node.value)
    elif isinstance(node, ast.Lambda):
        return "lambda"
    elif isinstance(node, ast.DictComp):
        return "dict"
    elif isinstance(node, ast.ListComp):
        return "list"
    elif isinstance(node, ast.GeneratorExp):
        return "generator"
    elif isinstance(node, ast.Call):
        func_name =get_func_calls(node) 
        func_name = func_name[0]
        if isinstance(node.func, ast.Name):
            if node.func.id == "dict":
                return "dict"
            elif node.func.id == "list":
                return "list"
            elif node.func.id == "tuple":
                return "tuple"
            elif node.func.id == "set":
                return "set"
            elif node.func.id == "str":
                return "str"
            elif node.func.id in ["id", "sum", "len", "int", "float", "ceil", "floor", "max", "min"]:
                return "num"
            elif node.func.id in ["all", "any", "assert", "bool"]:
                return "NC"
            elif node.func.id in ["iter"]:
                return "iterator"
            elif node.func.id in ["isinstance"]:
                return "NC"
            elif node.func.id in ['bytes']:
                return "bytes"
            elif is_camel_case(func_name):
                return func_name
            else:
                return "call"
        elif is_camel_case(func_name.split(".")[-1]):
            return func_name
        elif func_name in ['join', 'format']:
            return "str"
        else:
            return "call"
    elif isinstance(node, ast.Attribute):
        return "attr"
    else:
        return "unknown"

def name_formating_single(func_name, import_dict, class2obj = None):

    bo_obj = True
    bo_import = True
    name_parts = func_name.split('.')

    # this is a member function call but not a call chain
    if class2obj is not None:
        if name_parts[0] in class2obj and len(name_parts)==2:
            name_parts[0] = class2obj[name_parts[0]] 
        else:
            bo_obj = False

    if name_parts[0] in import_dict:
        name_parts[0] = import_dict[name_parts[0]]
    else:
        bo_import = False

    if class2obj == None and bo_import == False:
        return None
    if bo_obj == False and bo_import == False:
        return None
    return ".".join(name_parts)

def name_formating(import_dict, class2obj, alias_pair, func_names):

    full_name_lst = []
    alias_dict  = {e[0]:e[1] for e in alias_pair}

    for func_name  in func_names:
        name_parts = func_name.split('.')
        if name_parts[0] == 'self':
            continue

        alias_name = get_right_alias(alias_pair, class2obj, name_parts[0])
        if alias_name is not None:
            name_parts[0] = alias_name
        # this is a member function call but not a call chain
        if name_parts[0] in class2obj and len(name_parts)==2:
            name_parts[0] = class2obj[name_parts[0]]
        #  and the first part in the typebase

        # recover its qualified name
        if name_parts[0] in import_dict:
            name_parts[0] = import_dict[name_parts[0]]

        API_name = ".".join(name_parts)
        full_name_lst += [API_name]

    return full_name_lst
