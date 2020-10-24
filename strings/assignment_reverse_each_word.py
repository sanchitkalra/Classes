def reverseEachWord(string):
    arr = string.split()
    arr = [ x[::-1] for x in arr ]
    result = " ".join(arr)
    return result

string = input()

print(reverseEachWord(string))