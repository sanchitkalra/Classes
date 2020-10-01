# code is still wip

def checkNumber(number):

    a1 = 0
    a2 = 1

    i = 1

    while i <= number:
        a_n = a1 + a2
        a1 = a2
        a2 = a_n
        i += 1
    
    if a1 == number:
        return True
    else:
        return False