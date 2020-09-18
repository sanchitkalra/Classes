op = int(input())

while op!=6:
    if op >=1 and op <= 5:
        a = int(input())
        b = int(input())
    if op == 1:
        print(a+b)
    elif op == 2:
        print(a-b)
    elif op == 3:
        print(a*b)
    elif op == 4:
        print(a//b)
    elif op == 5:
    	print(a%b)
    elif op>6:
        print("Invalid Operation")
    op = int(input())