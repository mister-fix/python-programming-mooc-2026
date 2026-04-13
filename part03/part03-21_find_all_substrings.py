input_string = input("Please type in a word: ")
char = input("Please type in a character: ")
index = 0

while index < len(input_string):
    index = input_string.find(char, index)
    
    if index == -1 or index > len(input_string) - 3:
        break
    
    print(input_string[index:index+3])
    index = index + 1