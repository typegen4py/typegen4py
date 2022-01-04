
x = {"a":10}

def fun_out_of_class():
    return x
class A:
    def __init__(self):

        pass
    def fun(self): 

        return fun_out_of_class()
