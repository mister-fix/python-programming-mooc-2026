input_string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = input_string.find(substring)

if index >= 0:
    index2 = input_string.find(substring, index + len(substring))

    if index2 != -1:
        print(f"The second occurrence of the substring is at index {index2}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")