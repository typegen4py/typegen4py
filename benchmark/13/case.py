
from util import other_module_fun
from util import ParentA

class A(ParentA):

    def __init__(self):
        pass

    def fun(self):
        return super().fun()
