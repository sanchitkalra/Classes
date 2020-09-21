# k = int(input())

# rev = 0
# while (k > 0):
#     x = k % 10
#     rev = rev*10 + x
#     k = k//10
# print(rev)

def reverse(n):
    rev = 0
    while (n>0):
        x = n%10
        rev = rev*10 + x
        n = n//10
    return rev

n = int(input())
result = reverse(n)
print(result)