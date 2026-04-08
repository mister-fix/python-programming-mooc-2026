word = input("Word: ")
padding = 30 - len(word)
left_padding = (padding // 2) - 1
right_padding = padding - left_padding - 2

print("*" * 30)
print("*" + left_padding * " " + word + right_padding * " " + "*")
print("*" * 30)