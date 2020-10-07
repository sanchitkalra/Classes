# Print an inverted triangle pattern
# https://codezen.codingninjas.com/practice/463/649/pattern_ify

size = int(input())

for k in range(size, 0, -1):
    print("*"*k)