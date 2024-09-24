#Define the menu of restaurant

menu = {
    'Chole Bhature':40,
    'Puri Sabji':30,
    'Chola Samosa':30,
    'Samosa Chat':35,
    'Jalebi':10,
    'Chai':10
}

#Greet
print("Welcome to our restaurant")
for key,value in menu.items():
    print(key,":",value)

order_total = 0
item_1 = input("What do you want to order :").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your {item_1} is being prepared .")
else:
    print(f"{item_1} is not available please order something else.")

while True:
    reorder=input("Do you want something else ? (yes or no) : ").lower()
    if reorder == 'yes':
        item = input("What do you want to order :").title()
        if item in menu:
            order_total += menu[item]
            print(f"Your item {item} is placed .")
        else:
            print(f"{item} is not available please order something else.")
    elif reorder == 'no':
        print("Thank you for your order.")
        break
    else:
        print("Invalid Choice. Please Enter yes or no")

print(f"The total amount to be paid is :{order_total}")

