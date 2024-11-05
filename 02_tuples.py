### Tuple: ordered, immutable, allows duplicate elements
mytuple = ("Max", 28, "Boston") #Parantheses are optional
print(mytuple)

mytuple = ("Max",) #Single element tuple
print(type(mytuple))

mytuple = tuple(["Max", 28, "Boston"]) #List to tuple
print(mytuple)

# Accessing tuple elements
item = mytuple[0]
print(item)

# Negative indexing
item = mytuple[-1]
print(item)

# changing tuple elements
mytuple[0] = "Tim" #TypeError: 'tuple' object does not support item assignment

# Iterating over tuple
for i in mytuple:
    print(i)

# checking if element exists in tuple
if "Max" in mytuple:
    print("yes")
else:
    print("no")

# tuple length
mytuple = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple))

# count specific element
print(mytuple.count('p'))

# index of specific element
print(mytuple.index('p'))

# converting tuple to list
mylist = list(mytuple)
print(mylist)

# converting list to tuple
mytuple = tuple(mylist)
print(mytuple)

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)

b = a[:5]
print(b)

b = a[2:]
print(b)

# step index
b = a[::2]
print(b)

# reversing tuple
b = a[::-1]
print(b)

# unpacking
mytuple = "Max", 28, "Boston"
name, age, city = mytuple
print(name)
print(age)
print(city)

# unpacking with *; allows to unpack multiple elements into a list
mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)

# Working with tuples can be more efficient than lists, moreso working with large data sets
# See size comparison below
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Time comparison
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
# Tuples are faster than lists
