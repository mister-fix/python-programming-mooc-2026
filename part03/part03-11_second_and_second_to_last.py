input_string = input("Please type in a string: ")
secondChar = input_string[1]
secondToLastChar = input_string[-2]

if secondChar == secondToLastChar:
    print("The second and the second to last characters are", secondChar)
else:
    print("The second and the second to last characters are different")