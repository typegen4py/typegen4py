import ast
import os
import re
import sys
import json
import random
import astunparse
from copy import deepcopy
from core.func_call_visitor import get_func_calls, get_call_type
import _ast
from util import  tell_type,  get_path_by_extension
#from import_graph.import_graph import ImportGraph, Tree
import tarfile
from zipfile import ZipFile
from pkg_resources import parse_version
random.seed(100)


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

def is_valid_return(value):
    if value is None:
        return False
    if isinstance(value, ast.Constant):
        if value.value==None:
            return False
    if isinstance(value, ast.Constant):
        if value.value==None:
            return False
    if isinstance(value, ast.Name):
        if value.id=="NoReturn":
            return False
        if value.id=="Any":
            return False
        if value.id=="None":
            return False
    return True

def process_single_module(code):
    ast_tree = ast.parse(code)
    fun_nodes, class_nodes, import_nodes = parse_module(ast_tree) 
    n_returns = 0
    fun_name_lst = []
    for f_node in fun_nodes:
        r_val = f_node.returns
        if is_valid_return(r_val):
            n_returns += 1 
            fun_name_lst += [f_node.name]
    for c_node in class_nodes:
        class_name = c_node.name
        for  stmt in c_node.body:
            if isinstance(stmt, ast.FunctionDef):
                r_val = stmt.returns
                if is_valid_return(r_val):
                    fun_name_lst += [class_name+"."+stmt.name]
                    n_returns += 1

    return n_returns, fun_name_lst

def read_stub_types(code):
    ast_tree = ast.parse(code)
    fun_nodes, class_nodes, import_nodes = parse_module(ast_tree) 
    n_returns = 0
    fun_name_lst = []
    shed_type_dict = {}
    for f_node in fun_nodes:
        r_val = f_node.returns
        shed_type_dict[f_node.name] = r_val

    for c_node in class_nodes:
        class_name = c_node.name
        for  stmt in c_node.body:
            if isinstance(stmt, ast.FunctionDef):
                r_val = stmt.returns
                shed_type_dict[class_name+"."+stmt.name] = r_val

    #return n_returns, fun_name_lst
    return shed_type_dict

def lookup_typeshed_single(fn):
    code = open(fn).read()
    return process_single_module(code)

#def lookup_typeshed(base_dir, ep_name):
def lookup_typeshed(lib_dir):
    #ep = '../typeshed/stubs/'+ lib_name
    # ep = 'stub-exp/'+ lib_name
    all_stub_files = get_path_by_extension(lib_dir,  flag="pyi" )
    n_all = 0
    for fn in all_stub_files:
        #if lib_name != "six":
        #    continue
        code = open(fn).read()
        n_returns, fun_name_lst = process_single_module(code)
        #for name in fun_name_lst:
        #    src_name = os.path.basename(fn)
        #    src_name = src_name.rstrip(".pyi")
            #dir_name = os.path.dirname(fn)
            #dir_name = dir_name.lstrip(base_dir)
            #dir_name = dir_name.replace('/', '.')
            #full_name = "{}.{}.{}".format(dir_name.rstrip('.'),
            #        src_name.rstrip('.'),  name)
            #full_name = full_name.rstrip(".")
            #full_name = ep_name + "."+ full_name.lstrip('.')
            #names_segs = full_name.split('.')
            #if names_segs[0] == names_segs[1]:
            #    names_segs = names_segs[1:]
            #full_name = ".".join(names_segs)
        n_all +=  n_returns
    return n_all, len(all_stub_files)


def format_type_annot(annot):
    if isinstance(annot, ast.Name):
        return annot.id
    elif isinstance(annot, ast.Constant):
        return annot.value
    elif isinstance(annot, ast.Subscript):
        return format_type_annot(annot.value) 
    elif isinstance(annot, ast.Attribute):
        attr_name = get_attr_name(annot)
        return attr_name
    elif isinstance(annot, ast.Index):
        return format_type_annot(annot.value)
    elif isinstance(annot, ast.NameConstant):
        return format_type_annot(annot.value)
    else:
        return ast.dump(annot)

def test():
    lib_name = sys.argv[1]
    n_all, n_files = lookup_typeshed(lib_name)
    print(n_all, n_files)

if __name__ == '__main__':
   #main()
   test()
   #step4()

