MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")

def check(ordered_ingredients):
    for item in ordered_ingredients:
        if resources[item] < ordered_ingredients[item]:
            print("Sorry, insufficient resources.")
            return False
    return True

def process_coin():
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def make_coffee(coffee_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {coffee_name} ☕️")

def is_success(amount_received, drink_cost):
    global profit
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Shutting down...")
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if check(drink["ingredients"]):
            payment = process_coin()
            if is_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
