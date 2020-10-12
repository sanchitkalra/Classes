# examples of using the map function

# square all elements by a certain value
arr = [1, -2, 3, 4, -5, 6, 7]

def square(x):
    return x**2

arr = list(map(square, arr))
print(arr)

# find the absolute values for each element
arr = [1, -2, 3, 4, -5, 6, 7]

arr = list(map(abs, arr))
print(arr)

# using lambda functions as a map argument
arr = [1, -2, 3, 4, -5, 6, 7]

arr = list(map(lambda x: x if x >= 0 else -x, arr)) # this also gives the absolute value of the element using a lambda function
print(arr)