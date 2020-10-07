# Separate characters into 3 groups
# https://codezen.codingninjas.com/practice/8546/463/find-character-case

char = input()

if (ord(char) >= 65) and (ord(char) <= 90):
    print(1)
elif (ord(char) >= 97) and (ord(char) <= 122):
    print(0)
else:
    print(-1)