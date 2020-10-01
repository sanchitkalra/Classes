def numRev(n):
    rev = 0
    while (n>0):
        x = n%10
        rev = rev*10 + x
        n = n//10
    return rev

def checkPalindrome(n):
    if n == numRev(n):
        return True
    else:
        return False

n = int(input())
if checkPalindrome(n):
    print("true")
else:
    print("false")