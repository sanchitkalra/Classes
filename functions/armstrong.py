def checkArm(number):
    number = number

    array = []
    sum  = 0

    counter = 0

    for i in str(number):
        counter+=1

    print(counter)

    for i in range(0, counter):
        array.append(str(number)[i])

    for i in array:
        temp = int(i)**counter
        sum = sum + temp

    print("the summation is: ", sum)

    if (sum==int(number)):
        print("number is armstrong")
        return True
    else:
        print("number is not armstrong")
        return False

checkArm(23)