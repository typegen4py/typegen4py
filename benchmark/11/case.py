
class ParentA():
    def fun():
        return set([1,2,3,4]) 

class A(ParentA):

    def __init__(self):
        pass

    def fun(self): 
        return super().fun()
