#armstrong number

def checkArm(number):
    number = number

    array = []
    sum  = 0

    counter = 0

    for i in number:
        counter+=1

    print(counter)

    for i in range(0, counter):
        array.append(number[i])

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

count = 0
arm_numbers = []

for i in range(0, 1000):
    if checkArm(str(i)):
        count += 1
        arm_numbers.append(i)
        print(i)


print("total armstrong numbers: ", count)
print("numbers: ")
print(arm_numbers)