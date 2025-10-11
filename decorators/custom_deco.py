def repeat_deco(func):
    def wrapper():
        print("This function will run multiple times:")
        func()
        func()
    return wrapper

@repeat_deco
def greet():
    print("Hello, World!")
greet()