number = input()
even = 0
odd = 0

for k in number:
    if int(k)%2==0:
        even += int(k)
    else:
        odd += int(k)

print("{} {}".format(even, odd))