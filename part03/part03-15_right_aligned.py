input_string = input("Please type in a string: ")

if len(input_string) > 0:
    offset = 20 - len(input_string)

    if len(input_string) <= 20:
        print(f"{'*' * offset}{input_string}")