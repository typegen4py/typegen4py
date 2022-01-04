
class A():

    def __init__(self):
        pass
    def fun1(self): 
        return super().fun()
    def fun2(self): 
        return super().fun()
    def fun3(self): 
        return super().fun()

def unknown_func(any_val):
    return any_val.fun()
def test_fun():
    a = unknown_func()
    return a

res = test_fun()
res.fun1()
res.fun2()
res.fun3() 

