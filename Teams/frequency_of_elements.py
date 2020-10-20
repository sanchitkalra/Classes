# get frequency of all elements as a list and print them as tuples

arr = [1, 2, 1, 1, 1, 3, 4, 5, 6, 2, 8, 6, 4, 3, 2, 1, 1, 3, 4, 5, 6, 3, 4, 3, 3, 2, 4, 8]
smallest = min(arr)
largest = max(arr)

frequencies = []

for k in range(smallest, largest+1):
    frequency = arr.count(k)
    frequencies.append((k, frequency))

print(frequencies)