# CodeChef Problem: https://www.codechef.com/problems/HS08TEST

ask = float(input())
balance = float(input())

if ask%5 == 0:
    if balance >= (ask + 0.50):
        balance = balance - ask - 0.50
        print(balance)
    else:
        print(balance)
else:
    print(balance)
