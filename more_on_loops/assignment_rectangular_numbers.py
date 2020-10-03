## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for line in range(1, 2*n):
    a = n
    for col in range(1, 2*n):
        print(a, end = "")
        if col < line:
            a -= 1
        if col >= 2*n - line:
            a += 1
    print("")