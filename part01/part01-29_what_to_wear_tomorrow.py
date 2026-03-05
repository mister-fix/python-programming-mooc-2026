# Write your solution here
temperature_c = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
 
print("Wear jeans and a T-shirt")
 
if temperature_c <= 20:
    print("I recommend a jumper as well")
 
if temperature_c <= 10:
    print("Take a jacket with you")
 
if temperature_c <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
 
if rain == "yes":
    print("Don't forget your umbrella!")