degrees_f = int(input("Please type in a temperature (F): "))
degrees_c = ((degrees_f - 32) * 5) / 9
 
print(f"{degrees_f} degrees Fahrenheit equals {degrees_c} degrees Celsius")
 
if degrees_c < 0:
    print("Brr! It's cold in here!")