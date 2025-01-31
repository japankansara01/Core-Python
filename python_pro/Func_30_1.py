#function
def func_1():
    print("This is Function 1")

print("This is Print 1")
func_1()

#function to do arithmetic operation
def cal(a, b, c):
    total = a + b - c
    print(total)

x=1
y=2
z=5
cal(x, y, z)

#function
def isGreater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")

#calling function
isGreater(5,61)

#function arguments
#default, keyword, variable length, required arguments

#lambda function
add = lambda x, y: x + y
print(add(5, 3))