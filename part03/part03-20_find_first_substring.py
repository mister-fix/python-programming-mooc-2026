input_string = input("Please type in a word: ")
char = input("Please type in a character: ")

if char in input_string:
    index = input_string.find(char)
    
    if index >= 0 and index < len(input_string) - 2:
        print(input_string[index:index+3])