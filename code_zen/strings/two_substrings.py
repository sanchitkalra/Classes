string = input()

arr = []
for k in string:
    arr.append(k)

count = 0

k_i = -1

for k in range(len(arr)-1):
    if (arr[k] + arr[k+1] == "AB") or (arr[k] + arr[k+1] == "BA"):
        if k != k_i:
            count += 1
            k_i = k+1

if count >= 2:
    print("yes")
else:
    print("no")