size = 4

arr = [1, 5, 6, 9]
combinations = []

for k in range(size):
    for j in range(k+1, size):
        pair = (arr[k], arr[j])
        pair_r = (arr[j], arr[k])
        if (pair not in combinations) and (pair_r not in combinations):
            combinations.append(pair)

print(combinations)