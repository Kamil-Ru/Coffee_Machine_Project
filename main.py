
import coffee_data

resources = coffee_data.resources
menu = coffee_data.MENU
money_in_machine = 0


def asking_user_which_coffee():
    while True:
        user_typing = input("Hello, What would you like? (espresso/latte/cappuccino):\n").lower()
        if user_typing == "espresso":
            return menu["espresso"]
        elif user_typing == "latte":
            return menu["latte"]
        elif user_typing == "cappuccino":
            return menu["cappuccino"]
        elif user_typing == "report":
            print_report(resources, money_in_machine)
        elif user_typing == "q":
            return "q"


def print_report(resources, money_in_machine):
    """Report generate current resource values"""
    print(f"""
Water = {resources["water"]} ml
Milk = {resources["milk"]} ml
Coffee = {resources["coffee"]} g""")
    print("Money = $ {:.2f}".format(round(money_in_machine,2)))


def checking_resources(resources, user_coffee_ingredients):
    """Checking resources is sufficient, and return True if sufficient, or False."""
    if "water" in user_coffee_ingredients:
        if resources["water"] < user_coffee_ingredients["water"]:
            print("Sorry there is not enough water.")
            return False
    elif "milk" in user_coffee_ingredients:
        if resources["milk"] < user_coffee_ingredients["milk"]:
            print("Sorry there is not enough milk.")
            return False
    elif "coffee" in user_coffee_ingredients:
        if resources["coffee"] < user_coffee_ingredients["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    return True


def subtract_resources(resources, user_coffee_ingredients):
    if "water" in user_coffee_ingredients:
        resources["water"] -= user_coffee_ingredients["water"]

    if "milk" in user_coffee_ingredients:
        resources["milk"] -= user_coffee_ingredients["milk"]

    if "coffee" in user_coffee_ingredients:
        resources["coffee"] -= user_coffee_ingredients["coffee"]
    return resources


def counting_coins(user_coffee):
    """Checking money is sufficient.
    Print if is not enough money.
    Return change if is enough money."""
    while True:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        value_of_inserted_coins = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

        if user_coffee['cost'] > value_of_inserted_coins:
            print("Sorry that's not enough money. Money refunded.")

        elif user_coffee['cost'] <= value_of_inserted_coins:
            change = value_of_inserted_coins - user_coffee['cost']
            return change


while True:

    is_resources = False

    while is_resources is not True:
        # Coffee selection
        user_coffee = asking_user_which_coffee()
        if user_coffee == 'q':
            quit()

        user_coffee_ingredients = user_coffee["ingredients"]
        user_coffee_price = user_coffee["cost"]

        # Checking resources
        is_resources = checking_resources(resources, user_coffee_ingredients)


    # Counting and checking coins
    money_to_return = round(counting_coins(user_coffee), 2)

    # Adding coins too machine
    money_in_machine = money_in_machine + user_coffee_price


    # Subtract resources from machine,
    resources = subtract_resources(resources, user_coffee_ingredients)

    # Returning money
    print("Here is ${:.2f} dollars in change.".format(money_to_return))
    print("Here is your latte.Enjoy!")
