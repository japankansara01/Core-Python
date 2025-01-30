#Sequence

#List
a = [1, 2, "one"]
print(a)
#adding in list

a.append("123")
print(a)

#remove in list
a.remove(2)
print(a)

#change list item
lst = ["apple", "banana", "cherry"]
lst[1:2] = ["blackcurrant", "watermelon"]
print(lst)

#sort list
lst.sort(reverse=True)
print(lst)

#Tuple (can not perform any operation like list)
a = (1, 2 , "one")
print(a)
c = a[1]
print(c)


#Set
a = {1, 2, "one"}
print(a)

#String
a = "one"
print(a)


#map
a = {'1':'japan', '2':'abc'}  #1 is key , abc is value
print(a)
print(a.values())
print(a.get('1')) #get data from key