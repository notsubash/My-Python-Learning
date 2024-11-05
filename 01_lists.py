### Lists: ordered, mutable, allows duplicate elements

# Lists are defined by square brackets
mylist = ["football", "polo", "cricket"]
print(mylist)

#Can initialize an empty list like this
mylist2 = list()
print(mylist2)

#Can store multiple types in a list
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# Indexing of lists
item  = mylist[2]
print(item)

# Negative indexing is also supported
item  = mylist[-2]
print(item)

# loop through a list
for i in mylist:
    print(i)

# Check if an item is in a list
if "football" in mylist:
    print("Yes")
else:
    print("No")

# Get the length of a list
print(len(mylist))

# Append an item to a list
mylist.append("hockey")
print(mylist)

mylist.insert(1, "basketball")
print(mylist)

# Pop an item on the list
item = mylist.pop()
print(item)
print(mylist)

# Remove specific item
item = mylist.remove("polo")
print(item)
print(mylist)

# remove all elements
#mylist.clear()

#Reverse the list
mylist.reverse()
print(mylist)

# Sorting a list
mylist3 = [4,3,1,-1,-5, 10]
print(mylist3)
mylist3.sort()
print(mylist3)

# Sort the list and transfer to new list
new_list = sorted(mylist3)
print(new_list)

# Generating multiple lists
mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]

new_list = mylist + mylist2
print(new_list)

# Slicing of lists
mylist = [1,2,3,4,5,6,7,8,9]

a = mylist[1:5]
print(a)

a = mylist[:5]
print(a)

a = mylist[1:]
print(a)

# Stepping in slicing
a = mylist[::2]
print(a)

# Reverse a list
a = mylist[::-1]
print(a)

# Copying a list

# This way will affect the original list
list_org = ["buddha", "jesus","shiva"]
list_cpy = list_org
print(list_cpy)

list_cpy.append("krishna")
print(list_cpy)
print(list_org)

# This way will not affect the original list/ copy the list
list_org = ["buddha", "jesus","shiva"]
list_cpy = list_org.copy()
print(list_cpy)
list_cpy.append("krishna")
print(list_cpy)
print(list_org)

# This way will not affect the original list/ copy the list
list_org = ["buddha", "jesus","shiva"]
list_cpy = list(list_org)
print(list_cpy)
list_cpy.append("krishna")
print(list_cpy)
print(list_org)


# Last option to copy with slicing
list_org = ["buddha", "jesus","shiva"]
list_cpy = list_org[:]
print(list_cpy)
list_cpy.append("krishna")
print(list_cpy)
print(list_org)

# List comprehension
a = [1,2,3,4,5,6]
b = [i*i for i in a]
print(a)
print(b)


