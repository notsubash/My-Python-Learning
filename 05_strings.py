# Strings: ordered, immutable, text representation
my_string = 'I\'m a programmer!'
print(my_string)

# multi-line comment
my_string = """Hello \
World"""
print(my_string)

# slicing
my_string = "Hello World"
char = my_string[0]
print(char)

# we cannot change the change the character
my_string[0] = 'h'

#indexing
my_string = "Hello World"
substring = my_string[::-1]
print(substring)

# concatenate string
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# iterate
for i in greeting:
    print(i)

# checking for a substring
if 'ell' in greeting:
    print('yes')
else:
    print('no')

# whitespace removal
my_string = '   Hello World    '
my_string = my_string.strip()
print(my_string)

#convert to uppercase
my_string = 'Hello World'
print(my_string.lower())

#starts with
print(my_string.startswith('Hello'))

#find substring with index
print(my_string.find('lo'))

#count character
print(my_string.count('l'))

#replace substring
print(my_string.replace('World', 'Universe'))

#split string into list
my_string = 'how are you doing'
my_list = my_string.split(" ")
print(my_list)

##join list into string
new_string = ' '.join(my_list)
print(new_string)

# optimal way to concatenate string
from timeit import default_timer as timer
my_list = ['a'] * 1000000


#bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop=timer()
print(stop-start)
# print(my_string)

#good
start = timer()
my_string = ''.join(my_list)
stop=timer()
print(stop-start)
# print(my_string)

#formatting strings
# &, .format(), f-strings
var = 3.1234567
var2 = 6
my_string = "the variable is %.2f" %var ## %d is a placeholder for an integer and %s is a placeholder for a string
# %f is a placeholder for a float
print(my_string)

# .format()
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

# f-strings
my_string = f"the variable is {var:.2f} and {var2}"
print(my_string)