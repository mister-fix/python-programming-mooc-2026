attempts = 0

while True:
    pin = int(input("PIN: "))
    attempts = attempts + 1

    if pin == 4321:
        break
    
    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")