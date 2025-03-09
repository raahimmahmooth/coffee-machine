menu = {
    "Nestea": {
        "ingredients": {
            "water": 100,
            "Nestea_powder": 10,
            "Milk": 50
        },
        "cost": 110
    },
    "Nescafe": {
        "ingredients": {
            "water": 100,
            "Nestea_powder": 10,
            "Milk": 50
        },
        "cost": 110
    },
    "chai": {
        "ingredients": {
            "water": 100,
            "Milk": 100
        },
        "cost": 150
    },
}

profit = 0
resources = {
    "water": 1000,
    "Nestea_powder": 500,
    "Nescafe_powder": 500,
    "Milk": 1000
}

def password():
    passw = '123456'
    set_new=input("Set a New password or you can use the default password Type 'yes' or 'no':")
    if set_new=='yes':
        new_pass=input("Enter your password:")
        re_enter=input("Re-enter your password:")
        if new_pass == re_enter:
            print("You Password was changed.")
            passw=re_enter
        else:
            print("Password does not match.")
            passw=passw
    elif set_new=='no':
        print("Use your default password.")
        passw=passw
    else:
        print("Changing password was unsuccessful.")
        return False

    attempts = 3
    while attempts > 0:
        your_password = input("Enter maintainer password: ")
        if your_password == passw:
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
            if attempts == 0:
                print("Access denied.")
                return False


def make_coffee(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print("Pick up your coffee from the machine, Have a nice day Sir/Madam")

def check_payment(payment, coffee_cost, choice):
    if payment >= coffee_cost:
        global profit
        profit += coffee_cost
        change = payment - coffee_cost
        print(f"Your balance is {change}. Enjoy your {choice}!")
        return True
    else:
        print("Sorry, not enough money. Please try again!")
        return False

def payment_gateway():
    return int(input("Please input the money: "))

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def customer_portal():
    is_on = True
    while is_on:
        choice = input("What would you like to have? (Nestea/Nescafe/chai) or type 'back' to return: ")
        if choice == "back":
            is_on = False
        elif choice in menu:
            coffee_type = menu[choice]
            print(f"COST={coffee_type['cost']}")
            if check_resources(coffee_type["ingredients"]):
                payment = payment_gateway()
                if check_payment(payment, coffee_type['cost'], choice):
                    make_coffee(choice, coffee_type['ingredients'])
        else:
            print("Invalid choice. Please try again.")

def maintainer_portal():
    if password():
        is_on = True
        while is_on:
            choice = input("What would you like to do? (Report/Replenish) or type 'back' to return: ").lower()
            if choice == "back":
                is_on = False
            elif choice == "report":
                print(
                    f"water = {resources['water']} ml\nNestea_powder = {resources['Nestea_powder']} mg\nNescafe_powder = {resources['Nescafe_powder']} mg\nMilk = {resources['Milk']} mg\nProfit = {profit} Rs")
            elif choice == "replenish":
                for item in resources:
                    resources[item] += int(input(f"Enter amount to replenish {item}: "))
            else:
                print("Invalid choice. Please try again.")


def main():
    while True:
        user_type = input("Type 'Customer' or 'Maintainer' or 'exit' to quit: ").lower()
        if user_type == 'exit':
            print("Thank you for using the coffee machine. Goodbye!")
            break
        elif user_type == 'customer':
            customer_portal()
        elif user_type == 'maintainer':
            maintainer_portal()
        else:
            print("Invalid input. Please try again.")

# Run the program
main()