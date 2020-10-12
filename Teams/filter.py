# examples based on the filter function

# remove all negative value
arr = [1, -2, 3, 4, -5, 6, 7]

arr = list(filter(lambda x: True if x >= 0 else False, arr))
# a more compact way of writing the same expression:
# arr = list(filter(lambda x: x >= 0 , arr))
print(arr)

# remove all elements less than the mean
import statistics # to use an inbuilt function to calculate mean
arr = [1, -2, 3, 4, -5, 6, 7]

mean = statistics.mean(arr)

arr = list(filter(lambda x: x >= mean, arr))
print(arr)