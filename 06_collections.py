# collections: Counter, namedtuple, OrderedDict, defaultDict, deque
from collections import Counter
a = "aaaaabbbbbcccccc"
my_counter = Counter(a)
print(my_counter.values())

# index the counted list
print(my_counter.most_common(1)[0][0])

# elements 
print(list(my_counter.elements()))

####################################
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)


###############################
from collections import OrderedDict
ordered_dict = {}
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1
ordered_dict['e']=5
print(ordered_dict)

###########################
from collections import defaultdict
d = defaultdict(list) # Would raise a key error if normal dictionary is used
d['a'] = 1
d['b'] = 2
print(d['c'])

###########################
from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()

d.append(1)
d.append(2)
d.extend([4,5,6])
d.extendleft([7,8,9])
print(d)

d.rotate(2)
print(d)

d.rotate(-2)
print(d)