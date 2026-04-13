input_string = input("Please type in a string: ")

vowels = "aeo"

index = 0

while index < len(vowels):
    vowel = vowels[index]

    if vowel in input_string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
    
    index = index + 1