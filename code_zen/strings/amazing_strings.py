def createDict(string):
    dictionary = {}
    for k in string:
        dictionary[k] = dictionary.get(k, 0) + 1
    return dictionary

def addDict(dict1, dict2):
    result = {}
    keys_t = []
    for k in dict1:
        if k not in keys_t:
            keys_t.append(k)
    for k in dict2:
        if k not in keys_t:
            keys_t.append(k)
    keys = list(set(keys_t))
    for k in keys:
        result[k] = dict1.get(k, 0) + dict2.get(k, 0)
    return result

str1 = input()
str2 = input()
str3 = input()

if createDict(str3) == addDict(createDict(str1), createDict(str2)):
    print("YES")
else:
    print("NO")