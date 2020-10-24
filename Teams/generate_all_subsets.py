arr = [1, 2, 3]

subsets = [[]]

for k in range(len(arr)+1):
    for j in range(k+1, len(arr)+1):
        subsets.append(arr[k:j])

print(subsets)