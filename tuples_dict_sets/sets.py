# examples as the sets data structure

# create a set
s = {1, 2, "abc", 3, "xyz", 97}
print(s)

# create an empty set
empty_set = set()

# check type
print(type(s))

# sets are not indexed
# the following throws an error
#s[0]

# check for existence of an element in a set
print(1 in s) # returns True
print(45 in s) # returns False

# use for loop to iterate over elements
for x in s:
    print(x)

# get size of set
print(len(s))

# add elements to a set using the set.add() function
# parameters: (object)
s.add(48)

# update elements in a set using the set.update() function
# parameters: (set)
# does not affect any elements already present, only adds new elements which are not already present
y = {2, 3, 8, 6, 4, "hello", "new"}
s.update(y)
print(s)

# remove a specific element using set.remove() function
# parameters: (object)
# throws an error is the given object is not in the set
s.remove(1)
print(s)

# remove a specific element using the set.discard() function
# parameters: (object)
# does not throw an error if element is not present in the set
s.discard(1) # returns the set as is, 1 is not an element
s.discard(2) # returns the set after removing 2

# remove a random element from the set using set.pop()
# paramters: ()
s.pop()
print(s)

# remove all elements from the set
s.clear()
print(s)

# delete the set variable itself from memory
del s
#print(s)

# get intersection of two sets using set1.intersection(set2)
# parameters: (set)
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}

intersection = set1.intersection(set2)
print(intersection)

# get union of two sets using set1.intersection(set2)
# parameters: (set)

union = set1.union(set2)
print(union)

# get difference of two sets using set1.difference(set2)
# parameters: (set)

diff_one_minus_two = set1.difference(set2)
diff_two_minus_one = set2.difference(set1)
print("Set1 - Set2 = {}".format(diff_one_minus_two))
print("Set2 - Set1 = {}".format(diff_two_minus_one))

# get symmetric difference of two sets using set1.symmetric_difference(set2)
# parameters: (set)
# returns union-intersection
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)

# change set1 to the intersection of set1 and set2 using set1.intersection_update(set2)
# parameters: (set)
# has no return value
set1.intersection_update(set2)
print(set1)

# change set1 to the difference of set1 and set2 using set1.difference_update(set2)
# parameters: (set)
# has no return value
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}

set1.difference_update(set2)
print(set1)

# change set1 to the symmetric difference of set1 and set2 using set1.symmetric_difference_update(set2)
# parameters: (set)
# has no return value
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}

set1.symmetric_difference_update(set2)
print(set1)

# check is set1 is a subset of set2 using set1.issubset(set2)
# parameters: (set)
set3 = {1, 2, 3}
print(set3.issubset(set1))
print(set3.issubset(set2))

# check if set1 is a superset of set2 using set1.issuperset(set2)
# parameters: (set)
print(set1.issuperset(set3))
print(set2.issuperset(set3))

# check if two sets are disjoint using set1.isdisjoint(set2)
# parameters: (set)
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set2))