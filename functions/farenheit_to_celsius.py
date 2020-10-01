def printTable(start, stop, step):
    i = start
    while i <= stop:
        f = int((i-32)*(5/9))
        print(i, f)
        i += step

s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)