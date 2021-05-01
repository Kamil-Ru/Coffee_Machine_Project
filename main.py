# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO 3. Print report.
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.
import coffee_data

resources = coffee_data.resources
menu = coffee_data.MENU
money_in_machine = 0


def asking_user_wich_coffee():
    while True:
        user_typing = input("Hello, What would you like? (espresso/latte/cappuccino):\n").lower()
        if user_typing == "espresso":
            return menu["espresso"]
        elif user_typing == "latte":
            return menu["latte"]
        elif user_typing == "cappuccino":
            return menu["cappuccino"]
        elif user_typing == "report":
            print_report()
        elif user_typing == "q":
            return "q"


def print_report(resources=resources, money_in_machine=money_in_machine):
    '''Report generate current resource values'''
    print(f"""
    Water = {resources["water"]} ml
    Milk = {resources["milk"]} ml
    Coffee = {resources["coffee"]} g
    Money = $ {money_in_machine}""")


print_report()


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

    # "Sorry there is not enough water."
    # TODO 8 - REFACTOR - for x,y in resorce and .....


def subtract_resources(resources, user_coffee_ingredients):
    if "water" in user_coffee_ingredients:
        resources["water"] -= user_coffee_ingredients["water"]

    if "milk" in user_coffee_ingredients:
        resources["milk"] -= user_coffee_ingredients["milk"]

    if "coffee" in user_coffee_ingredients:
        resources["coffee"] -= user_coffee_ingredients["coffee"]

    return resources


# cos = checking_resources()
# print(cos)

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
        value_of_inserted_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        if user_coffee['cost'] > value_of_inserted_coins:
            print("Sorry that's not enough money. Money refunded.")

        elif user_coffee['cost'] <= value_of_inserted_coins:
            change = value_of_inserted_coins - user_coffee['cost']
            return change


# TODO ROUND !!


### COFFY Machin
# Test
game_on_TEST = True
money_in_machine = 0

while True:
    is_resorces = False
    while is_resorces is not True:
        # Coffee selection
        user_coffee = asking_user_wich_coffee()

        user_coffee_ingredients = user_coffee["ingredients"]
        user_coffee_price = user_coffee['cost']
        print(f"user_coffee_price = {user_coffee_price =}")
        # Checking resources
        print(checking_resources(resources, user_coffee_ingredients))
        is_resorces = checking_resources(resources, user_coffee_ingredients)

    #Test
    # print_report(resources, money_in_machine)

    # Counting and checking coins
    money_to_return = counting_coins(user_coffee)
    # Adding coins too machine
    money_in_machine = money_in_machine+user_coffee_price
    # print(f"user_coffee_price = {user_coffee_price}")
    # print(f"money_in_machine = {money_in_machine}")
    # Subtract resources from machine,
    resources = subtract_resources(resources, user_coffee_ingredients)
    # Returning money
    print(f"Here is ${money_to_return} dollars in change.")
    print("Here is your latte.Enjoy!")


