marks = int(input("enter marks: "))

if marks in range(90, 100):
    print("Grade O")
elif marks in range(80, 90):
    print("Grade A")
elif marks in range(70, 80):
    print("Grade B")
elif marks in range(60, 70):
    print("Grade C")
else:
    print("Give the exam again")


if marks >= 90 and marks <=100:
    print("Grade O")
elif marks >= 80 and marks <=90:
    print("Grade A")
elif marks >= 70 and marks <=80:
    print("Grade B")
elif marks >= 60 and marks <=70:
    print("Grade C")
else:
    print("Give the exam again")