# Errors and Exceptions

# Syntax Error
a = 5 
print (a))

#Type error
a = 5 + '10'

#import error
import somemodule

# Name error
a = 5
b = c

# File not found error
f = open('somefile.txt')

#value error
a = [1,2,3]
a.remove(4)
print(a)

# index error
a = [1,2,3]
a[4]

# Key error
my_dict = {'name':'Max'}
my_dict['age']

##################### Forcing an exception
x = -5
if x < 0:
    raise Exception('x should be positive.')

#using assert
x = -19
assert(x >= 0), 'x is not positive'

######### Handle exceptions
try:
    a = 5 / 1
    b = a + 2
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')

# Custom exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
    
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)