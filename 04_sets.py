# Sets: unordered, mutable, no duplicates
myset = {1,2,3,1,2}
print(myset)

myset = set("Hello")
print(myset)

#This way it initializes an empty dictionary rather than a set
myset= {}
print(type(myset))

myset = set()
print(type(myset))

# Adding elements
myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(4) #gives no eror
myset.remove(3)

#empty the set
myset.clear()

# removing element
myset.pop()

print(myset)

# iterate through the set
for i in myset:
    print(i)

#checking element in set
if 1 in myset:
    print("yes")

####################################
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#Union
u = odds.union(evens)
print(u)

# intersection
i = odds.intersection(primes)
print(i)

# Difference of two sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

# symmetric difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.symmetric_difference(setB)
print(diff)

# update setA with elements in setB
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.update(setB)
print(setA)

# intersection update
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.intersection_update(setB)
print(setA)

# difference update
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.difference_update(setB)
print(setA)

# symmetric difference update
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.symmetric_difference_update(setB)
print(setA)

# subset
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setB.issubset(setA))

# superset
setA = {1,2,3,4,5,6}
setB = {1,2,3}
print(setA.issuperset(setB))

# disjoint
setA = {1,2,3,4,5,6}
setB = {7,8,9}
print(setA.isdisjoint(setB))

# copy sets
# This way will change both sets
setA = {1,2,3,4,5,6}
setB = setA
print(setB)
setB.add(7)
print(setA)
print(setB)

# choose these two ways to copy sets without changing both sets
setA = {1,2,3,4,5,6}
setB = setA.copy()
print(setB)
setB.add(7)
print(setA)
print(setB)

setA = {1,2,3,4,5,6}
setB = set(setA)
print(setB)
setB.add(7)
print(setA)
print(setB)

#  Frozen set
# immutable and hashable. cannot use add, remove, update but works with union, intersection, difference
a = frozenset([1,2,3,4])
a.remove(1)
print(a)
