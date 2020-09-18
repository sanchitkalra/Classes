#Simple Interest

principal = int(input("principal: "))
rate = int(input("rate of interest: "))
time = int(input("time period: "))

si = principal*rate+time

print("Interest: ", si)
print("Amount after ", time, " is ", (principal+si))