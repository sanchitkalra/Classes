def replace(string, key, replacement):
    count = string.count(key)
    for k in range(count):
        string = string.replace(key, replacement)
    return string

string = input()
key = input()
replacement = input()

print(replace(string, key, replacement))