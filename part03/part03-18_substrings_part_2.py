input_string = input("Please type in a string: ")
index = 1

while index <= len(input_string):
    print(input_string[-index:])
    index = index + 1