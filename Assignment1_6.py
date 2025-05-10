def CheckNumber(num):
    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

number = int(input("Enter a number: "))
CheckNumber(number)
