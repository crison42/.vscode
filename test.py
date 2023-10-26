def deco(func):
    def wrapper():
        print(f"before {func.__name__} called.")
        func()
        print(f"after {func.__name__} called.")
    return wrapper

@deco
def myfunc1():
    print("myfunc1() called.")

@deco
def myfunc2():
    print("myfunc2() called")

myfunc1()
myfunc2()

# Output:
# before myfunc1 called.
# myfunc1() called.
# after myfunc1 called.
# before myfunc2 called.
# myfunc2() called
# after myfunc2 called.