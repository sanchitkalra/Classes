pay_and_grade = input().split()
pay = int(pay_and_grade[0])
grade = pay_and_grade[1]

hra = 0.2*pay
da = 0.5*pay
pf = 0.11*pay
allow = 0

if grade == "A":
    allow = 1700
elif grade == "B":
    allow = 1500
else:
    allow = 1300

total = round(pay+hra+da-pf+allow)
print(total)