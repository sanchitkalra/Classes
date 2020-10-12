# examples on using the reduce function
'''

The reduce function essentially works as following:
assume an array, arr = [a, b, c, d, e, f]
and we have to apply a function f to the iterable's elements

the execution proceeds as follows

val1 = f(a, b)
val2 = f(val1, c)
val3 = f(val2, d)
...

'''

# import functools to access the reduce function
import functools

# calculate the sum of all elements
arr = [1, -2, 3, 4, -5, 6, 7]

sum = functools.reduce(lambda x, y: x + y, arr) # the reduce function directly returns a list
print(sum)

# calculate the product of all elements
arr = [1, -2, 3, 4, -5, 6, 7]

prod = functools.reduce(lambda x, y: x*y, arr)
print(prod)