import math

a = input("Enter to number 1: ")
b = input("Enter to number 2: ")

number = input(" 1.Sum \n 2.Subtract \n 3.Mul \n 4.Divide \n 5.Reminder \n 6.Square \n 7.Sqrt \nEnter Choice:")

if number == "1":
    print(int(a)+int(b))
elif number == "2":
    print(int(a)-int(b))
elif number == "3":
    print(int(a)*int(b))
elif number == "4":
    print(int(a)/int(b))
elif number == "5":
    print(int(a)%int(b))
elif number == "6":
    print(int(a)**int(b))
elif number == "7":
    print(math.sqrt(int(a)),math.sqrt(int(b)))
else:
    print("Invalid Option!")  