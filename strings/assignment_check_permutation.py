def checkPermutation(str1, str2):
    d_str1 = {}
    d_str2 = {}
    for k in str1:
        d_str1[k] = d_str1.get(k, 0) + 1
    for k in str2:
        d_str2[k] = d_str2.get(k, 0) + 1
    if d_str1 == d_str2:
        return True
    else:
        return False

str1 = input()
str2 = input()

if checkPermutation(str1, str2):
    print("true")
else:
    print("false")