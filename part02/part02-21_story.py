string = ''
prev = ''

while True:
    word = input("Please type in a word: ")

    if prev == word:
        break
    else:
        prev = word
        
    if word == "end":
        break
    
    string = string + word + ' '

print(string)