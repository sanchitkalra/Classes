def removeConsecutiveDuplicates(string):
    li=[]
    i=0
    for char in string:
        li.append(char)
    while i < len(li)-1:
        if li[i] == li[i+1]:
            del li[i]
        else:
            i = i+1
    str = "".join(li)
    print(str)

string = input()
removeConsecutiveDuplicates(string)

# def removeConsecutiveDuplicates(string):
#     arr = []
#     for k in range(len(string)):
#         if (k != len(string) - 1):
#             if string[k] != string[k+1]:
#                 arr.append(string[k])
#         else:
#             if string[k] == string[k-1]:
#                 arr.append(string[k])
#     result = ""
#     for k in arr:
#         result += k
#     return result

# string = input()

# print(removeConsecutiveDuplicates(string))