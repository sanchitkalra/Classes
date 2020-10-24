# examples based on the dictionary data structure

# create a dict
dictionary = {"a": 1, "b": 2, "c": 3}

# print the dict
print(dictionary)

# return the type
print(type(dictionary))

# get size
print(len(dictionary))

# copy a dict into another variable
dict2 = dictionary.copy()
print(dict2)

# use zip to create a dict
# parameters: (keys, values), keys, values both are iterables
keys = [1, 2, 3]
values = ["a", "b", "c"]
dict3 = dict(zip(keys, values))
print(dict3)

# create a dict using a list of tuples
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
dict4 = dict(list_of_tuples)
print(dict4)

# create a dict using the dict.fromkeys() function
# paramters: (keys(mandatory), value(optional)), keys is an iterable, value is any object
# this function sets the default value for all key-value pairs to be None unless a value is explicitly specified in which case it sets it to be the value for all key-value pairs
dict5 = dict.fromkeys(["a", "b", "c"])
print(dict5)

dict6 = dict.fromkeys(["a", "b", "c"], 100)
print(dict6)

# access a specific element in the dict
# syntax: dict[key]
# returns an error is the key-value pair is not found in the dict
dictionary = {"a": 1, "b": 2, "c": 3}
print(dictionary["a"])

# elements can also be accessed using the dict.get() function
# parameters: (key(mandatory), default(optional))
# note: the function returns a None object is the key-value pair is not found in the dict unless default is specified in which case default is returned
print(dictionary.get("b")) # returns 2
print(dictionary.get("d")) # returns None
print(dictionary.get("e", 0)) # returns 0

# get all keys from dict
print(dictionary.keys())

# get all values from dict
print(dictionary.values())

# get all key value pairs from dict as a list of tuples
print(dictionary.items())

# using loops with dict
# using only one variable with a for loop returns the keys
# using two parameters with a for loop returns both the keys and the values, see example below
for k in dictionary: # print all keys
    print("key is {}".format(k))

for key_x, value_x in dictionary.items(): # print key-value pairs
    print("key is {} and value is {}".format(key_x, value_x))

for value in dictionary.values(): # print all values
    print("value is {}".format(value))

# check if a key is present in a dict
# syntax: key in dict, see example
print("a" in dictionary)
print("d" in dictionary)

# add a key-value pair to a dict
dictionary["key"] = 4
print(dictionary)

# update a key-value pair in a dict
dictionary["a"] = 5
print(dictionary)

# update multiple key-value pairs in a dict using dict.update()
# parameters: (dict)
# this updates existing pairs as per the dictionary passed to the function and creates new pairs for non existing values
more_elements = {"a": 10, "b": 100, "d": 1010, "e": 99}
dictionary.update(more_elements)
print(dictionary)

# remove elements from a dict with dict.pop()
# parameter: (key)
# produces a value error is key is not present in the dict
dictionary.pop("a")
print(dictionary)

# remove element with the del keyword
del dictionary["b"]
print(dictionary)

# clear the entire dict
# the dict varible is still present as an empty dictionary after this operation
dictionary.clear()
print(dictionary)

# delete the dict from memory
del dictionary
#print(dictionary)