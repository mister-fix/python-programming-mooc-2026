# Write your solution here
cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
weekly_groceries = float(input("How much money do you spend on groceries in a week? "))
 
weekly = (lunch_price * cafeteria_visits) + weekly_groceries
 
print("Average food expenditure:")
print(f"Daily: {weekly / 7} euros")
print(f"Weekly: {weekly} euros")