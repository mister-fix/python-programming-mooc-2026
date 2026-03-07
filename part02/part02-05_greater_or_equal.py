number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number: "))

if number1 > number2:
    print("The greater number was:", number1)
elif number2 > number1:
    print("The greater number was:", number2)
else:
    print("The numbers are equal!")