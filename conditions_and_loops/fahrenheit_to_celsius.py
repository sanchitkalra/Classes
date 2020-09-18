start = int(input())
end = int(input())
step = int(input())

i = start

while i <= end:
    f = int((i - 32)*(5/9))
    print(i, "", f)
    i += step