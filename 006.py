from datetime import date
today = date.today()

birthYear = int(input("Your birthyear? "))
age = today.year - birthYear
print(age)
if 15 <= age <= 20:
    print("teenager XD")
