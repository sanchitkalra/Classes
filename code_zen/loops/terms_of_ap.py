n=int(input())
i=1
count=0
while count<n:
    x=(3*i)+2
    if not(x%4==0):
        print(x,end=' ')
        count+=1
    i=i+1

# terms = int(input())

# i = 1
# while i <= terms:
#     x = (3*i) + 2
#     if not (x%4 == 0):
#         print(x, end = " ")
#         i += 1