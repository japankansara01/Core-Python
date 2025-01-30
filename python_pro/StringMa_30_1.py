#concatination in string
from os.path import split

a = "abc" + "acb"
print(a)

#string slicing
a = "Hello World!"
print(a)
b = a[8]
print(b)
b = a[8:10]
print(b)

#replacing string
a = "ABC"
a1 = a.replace("ABC","BCD")
print(a1)

#split and join strings
x = "Welcome to -alian software"
y = x.split("-")
print(y)
y = "-".join(x)
print(y)

#properties checking
a = "Hello"
print(a.startswith("H"))
print(a.endswith("o"))

#formatting in string
a = "japan"
b = 22
msg = f"My name is {a} and my age is {b}"  #f prefix is mandatory here
print(msg)