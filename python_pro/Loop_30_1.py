#for loop
color = ["black","white","yellow"]
for i in color:
    print(i)

#basic pattern
l = 3
for i in range(1, l+1):
    for j in range(1, i+1):
        print("*",end=" ")
    print()

#while loop
i = 2
while i<=1:
    print("Hello")
    j=2
    while j<=1:
        print("World")
        j=j+1
    i=i+1

#if-else loop
x = 10
y = 20
z = 15
if x > y and x > z:
    print("x is the largest")
elif y > x and y > z:
    print("y is the largest")
else:
    print("z is the largest")


#for loop
#continue, break, pass statements