x=5
def myFunc():
    x=11
    y=9
    print(x,y)

myFunc()
print(x)



def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)
abc=str(78)
print(type(abc), "k ho?")
x = {"name" : "John", "age" : 36}
print(type(x))