
x = {"a":10}
class A:
    def __init__(self):
        pass

    def _fun(self):
        
        return x

    def fun(self):
        
        return self._fun()
