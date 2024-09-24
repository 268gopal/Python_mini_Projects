rent = int(input("Room Rent :"))
food = int(input("Food Expense :"))
electricity = int(input("Electricity Bill :"))
water = int(input("Water Bill :"))
Persons = int(input("Number of person :"))

Total_bill = rent + food + electricity + water

each_expense = Total_bill / Persons

print(f"Each person has to pay Rs.{each_expense} for this month.") 