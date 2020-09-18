num = int(input())

count = 0

n_str = str(num)

odd_sum = 0
even_sum = 0

for i in n_str:
    count+=1

i = 0    
    
while i < count:
    y = int(n_str[i])
    if y%2 == 0:
        even_sum += int(n_str[i])
    else:
        odd_sum += int(n_str[i])
    i += 1
        
print(even_sum, " ", odd_sum) 