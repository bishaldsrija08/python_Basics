# Function

def greet(name):
    print(f"hello {name}")
greet("bishal")


def add(a,b):
    return (a+b)

result = add(4,5)
print(result)

# Lambda function in python
add = lambda a,b: a+b
print(add(5,6))



def test(*args):
    for arg in args:
        print (arg)
    
    
test(2,3,4)


def is_even(num):
    return num%2==0

result = is_even(330)
print(result)