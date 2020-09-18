# Converts a binary number to a decimal number

binary = int(input("Enter a binary number: "))

b_str = str(binary)
b_arr = []
decimal = 0

for i in b_str:
    b_arr.append(i)

b_arr.reverse()

i = 0
while i < len(b_arr):
    temp = int(b_arr[i])*(2**i)
    decimal = decimal + temp
    i += 1

print(decimal)