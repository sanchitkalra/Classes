def removeAllOccurances(string, chr):
    result = ""
    for k in string:
        if k != chr:
            result += k
    return result

string = input()
chr = input()

print(removeAllOccurances(string, chr))