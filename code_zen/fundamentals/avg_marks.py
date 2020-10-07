# Average Marks problem
# https://codezen.codingninjas.com/practice/8546/955/average-marks

name = input()

marks = [int(value) for value in input().split()]

sum = 0

for k in marks:
    sum += k

print(name)
print(sum//3)