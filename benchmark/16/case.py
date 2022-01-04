
def fun1(a):
    if a>10:
        return True
    return False

def func2(a):
    return a.mean()

fun1(func2())
fun1(10)
