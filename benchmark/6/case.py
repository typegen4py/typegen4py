x = {"a":10}
class A:
    def __init__(self):
        pass

    def fun(self):
        x["b"] = 20
        return x 
