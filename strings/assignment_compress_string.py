def compressString(string):
    i = 0
    li = []
    result = ""
    count = 1
    for k in string:
        li.append(k)
    while i < len(li)-1:
        if li[i] == li[i+1]:
            del li[i+1]
            count += 1
        else:
            if count == 1:
                result += li[i]
            else:
                result += li[i] + str(count)
            count = 1
            i += 1
    print(li)
    if count == 1:
        result += li[-1]
    else:
        result += li[-1] + str(count)
    return result

print(compressString("aaabbccdsa"))