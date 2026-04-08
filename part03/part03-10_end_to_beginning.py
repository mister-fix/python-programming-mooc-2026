input_string = input("Please type in a string: ")
length = len(input_string)

while length > 0:
    print(input_string[length - 1])
    length -= 1