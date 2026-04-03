upper_limit = int(input("Limit: "))
number = 1
total = 0
string = ""

while total < upper_limit:
    total = total + number
    if number > 1:
        string += " + "
    string += f"{number}"
    number = number + 1

print(f"The consecutive sum: {string} = {total}")