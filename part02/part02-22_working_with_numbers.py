tracker = 0
sum = 0
positives = 0
negatives = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    
    sum = sum + number
    tracker = tracker + 1

    if number > 0:
        positives = positives + 1
    if number < 0:
        negatives = negatives + 1

print("... the program asks for numbers")
print(f"Numbers typed in {tracker}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / tracker}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")