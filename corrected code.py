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
            "Nescafe_powder": 10,
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

stored_password = "123456"  # Maintainer password


def set_password():
    global stored_password
    choice = input("Set a new password? Type 'yes' or 'no': ").lower()

    if choice == 'yes':
        new_pass = input("Enter new password: ")
        re_enter = input("Re-enter password: ")
        if new_pass == re_enter:
            stored_password = new_pass
            print("Password changed successfully.")
        else:
            print("Passwords do not match. Keeping the old password.")
    elif choice == 'no':
        print("Using the default password.")
    else:
        print("Invalid option.")


def authenticate():
    attempts = 3
    while attempts > 0:
        entered_password = input("Enter maintainer password: ")
        if entered_password == stored_password:
            return True
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")
    print("Access denied.")
    return False


def check_resources(order_ingredients):
    """Check if enough resources are available."""
    for item, amount in order_ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_payment(coffee_cost):
    """Handle customer payment with input validation."""
    while True:
        try:
            payment = int(input("Please input the money: "))
            if payment >= coffee_cost:
                change = payment - coffee_cost
                if change > 0:
                    print(f"Your change is {change} Rs.")
                global profit
                profit += coffee_cost  # Only adding the actual cost to profit
                return True
            else:
                print("Not enough money. Please try again.")
        except ValueError:
            print("Invalid input. Enter a number.")


def make_coffee(choice, ingredients):
    """Deduct resources and serve coffee."""
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {choice}. Enjoy!")


def customer_portal():
    """Customer interaction."""
    while True:
        choice = input("What would you like? (Nestea/Nescafe/chai) or type 'back' to return: ").capitalize()
        if choice == "Back":
            break
        elif choice in menu:
            coffee_type = menu[choice]
            print(f"COST = {coffee_type['cost']} Rs")

            if check_resources(coffee_type["ingredients"]):  # Check before payment
                if process_payment(coffee_type["cost"]):  # Process payment only if resources are enough
                    make_coffee(choice, coffee_type["ingredients"])
        else:
            print("Invalid choice. Please try again.")


def maintainer_portal():
    """Maintainer functions (report & replenish)."""
    set_password()
    if authenticate():
        while True:
            action = input("What would you like to do? (Report/Replenish) or type 'back' to return: ").lower()
            if action == "back":
                break
            elif action == "report":
                print(f"Water: {resources['water']} ml\nNestea Powder: {resources['Nestea_powder']} mg\n"
                      f"Nescafe Powder: {resources['Nescafe_powder']} mg\nMilk: {resources['Milk']} mg\n"
                      f"Profit: {profit} Rs")
            elif action == "replenish":
                for item in resources:
                    while True:
                        try:
                            amount = int(input(f"Enter amount to add to {item}: "))
                            resources[item] += amount
                            break
                        except ValueError:
                            print("Invalid input. Enter a number.")
            else:
                print("Invalid choice. Please try again.")


def main():
    """Main function to run the program."""
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
