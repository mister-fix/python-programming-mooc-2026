points = int(input("How many points [0-100]: "))
 
if points < 0 or points > 100:
    print("impossible!")
elif points >=0 and points <= 49:
    print("fail")
elif points >= 50 and points <= 59:
    grade = 1
    print("Grade:", grade)
elif points >= 60 and points <= 69:
    grade = 2
    print("Grade:", grade)
elif points >= 70 and points <= 79:
    grade = 3
    print("Grade:", grade)
elif points >= 80 and points <= 89:
    grade = 4
    print("Grade:", grade)
elif points >= 90 and points <= 100:
    grade = 5
    print("Grade:", grade)