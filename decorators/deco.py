def greet(func):
    def m_func(*args, **kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Good Night!")

    return m_func


# @greet
def add(a, b):
    print(a + b)


# @greet
def hello():
    print("Hello, World!")


# greet(hello)()
greet(add)(5, 7)