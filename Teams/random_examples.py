# examples based on the random module

import random

# generate a random number in a range with random.randint()
# parameters: (start, end) 
# start and end are both inclusive and integers
start = 0
end = 100
random_int = random.randint(start, end)
print("a random number between {} and {} is {}".format(start, end, random_int))

# generate a sample subset of an iterable using the random.sample() function
# parameters: (iterable, output-size)
# output-size <= length of iterable
# result is returned without replacement
iterable = [1, 2, 3, 4, 56, 67, 88, 5, 2, 2, 1]
length = 5
result = random.sample(iterable, length)
print("a sample list for {} of length {} is {}".format(iterable, length, result))

# generate a random number in a range with custom step size using random.randrange()
# parameters: (start, stop, step)
# start(optional, defaults to 0), stop(mandatory), step(optional, defaults to 1)
# all three parameters must be integers and stop > start
start = 10
stop = 100
step = 5
result = random.randrange(start, stop, step)
print("a random number between {} and {} with a step-size of {} is {}".format(start, stop, stop, result))

# shuffle an iterable using random.shuffle()
# parameters: (iterable)
# list must be an iterable of supported or defined data-types
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("arr before shuffle is {}".format(arr))
random.shuffle(arr)
print("arr after shuffle is {}".format(arr))

# choose a random element from an iterable using random.choice()
# parameters: (iterable)
# list must be an iterable of supported or defined data-types
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = random.choice(arr)
print("a random choice from {} is {}".format(arr, result))

# generate a random number between 0(inclusive) and 1(exclusive) using random.random()
# parameters: ()
print("a random number between 0 and 1 is {}".format(random.random()))

# generate a random number in a range using random.uniform()
# parameters: (start, end)
# start and end must both be either floats or integers
# the result is always a float
start = 10
end = 100
result = random.uniform(start, end)
print("a random number between {} and {} is {}".format(start, end, result))

# generate an iterable of k-size using a source array with custom weights using random.choices()
# parameters: (iterable(mandatory), weights(defaults to None), cum_weights(defaults to None), k(mandatory))
# weights and cum_weights parameters are NOT usable at the same time
# weights defines relative probabilities
# cum_weights define cumulative probabilities
# result is an array of size k with elements from the iterable
# repetition is allowed
arr = [1, 2, 3, 4, 5]

# using relative probabilities with weights parameter
# size of weights parameter must be same as the size of iterable
# probability of occurance of each element of iterable is weights[k]/(sum of elements of weights)
weights_arr = [10, 20, 60, 90, 10]
size = 10
result = random.choices(arr, weights=weights_arr, k=size)
print("arr generated from {} of size {} with relative probabilities {} is {}".format(arr, size, weights_arr, result))

# using absolute probabilities with cum_weights parameter
cum_weights_arr = [10, 30, 50, 90, 20]
size = 10
result = random.choices(arr, cum_weights=cum_weights_arr, k=size)
print("arr generated from {} of size {} with absolute probabilities {} is {}".format(arr, size, cum_weights_arr, result))

# generate pseudo-random numbers with the random.seed() method
# parameters: (seed_val)
seed_val = 10
random.seed(seed_val)
print("a random number with seed {} is {}".format(seed_val, random.random())) # try running this script multiple times, the value at this step will always be the same