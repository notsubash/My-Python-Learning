# Dictionary: Key-Value pairs, Unordered, Mutable

#Initializing dictionaries
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict2)

# Check values
value = my_dict["age"]
print(value)

# Adding new key-value pairs
my_dict["email"] = "max@xyz.com"
print(my_dict)

# Delete items
del my_dict["name"]
print(my_dict)

my_dict.pop("age")
print(my_dict)

my_dict.popitem()
print(my_dict)

# check for a value in dictionary
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

if "lastname" in my_dict:
    print(my_dict["lastname"])

try:
    print(my_dict["lastname"])
except:
    print("Error")

# Looping through a dictionaryy
for key, value in my_dict.items():
    print(key, value)

# Copying the dictionary
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)
my_dict_cpy = my_dict.copy()
my_dict_cpy["email"] = "max@xyz.com"
print(my_dict_cpy)
print(my_dict)

# Option-2
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)
my_dict_cpy = dict(my_dict)
my_dict_cpy["email"] = "max@xyz.com"
print(my_dict_cpy)
print(my_dict)

# Merge dictionaries
my_dict = {"name": "Max", "age": 28, "email":"max@xyz.com"}
my_dict2 = dict(name="Mary", age =27, city="Boston")

my_dict.update(my_dict2)
print(my_dict)

#Possible key types
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

#Can use tuple as key
my_tuple = (8,7) # Cannot use list as key
my_dict = {my_tuple: 15}
print(my_dict)