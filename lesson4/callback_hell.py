
def f1(f):
    print("f1")
    f(f3)

def f2(f):
    print("f2")
    f(f3)

def f3(f):
    print("f3")
    f(f4)

def f4(f):
    print("f4. That's it.")


f1(f2)
