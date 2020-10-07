# Print Alpha Pattern
# https://codezen.codingninjas.com/practice/463/661/alpha-pattern

size = int(input())

for k in range(size):
    for j in range(k+1):
        print(chr(ord("A")+k), end = "")
    print("")
