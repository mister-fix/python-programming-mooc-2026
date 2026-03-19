letter_1 = input("1st letter: ")
letter_2 = input("2nd letter: ")
letter_3 = input("3rd letter: ")
 
if letter_2 <= letter_1 <= letter_3 or letter_3 <= letter_1 <= letter_2:
    print("The letter in the middle is", letter_1)
elif letter_1 <= letter_2 <= letter_3 or letter_3 <= letter_2 <= letter_1:
    print("The letter in the middle is", letter_2)
else:
    print("The letter in the middle is", letter_3)