class A:
    def __init__(self):
        pass
    def __eq__(self):
        return "str"
    def __len__(self):
        return "str"
    def fun(self):
        return True
    def iter(self):
        for i in range(10):
            yield i

    def test_bool(self):

        return True
