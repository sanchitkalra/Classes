def getHighestOccuringChr(string):
    str_d = {}
    for k in string:
        str_d[k] = str_d.get(k, 0) + 1
    index = max(str_d.values())
    max_key = None
    for key, value in str_d.items():
        if value == index:
            max_key = key
            break
    return max_key

string = input()

print(getHighestOccuringChr(string))