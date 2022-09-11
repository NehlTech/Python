
# """1. Prompt user by asking 'What would you like? (expresso/latte/cappuccino):'"""
# """a. Check the user's input to decide what to do next."""
# """b. The prompt should show every time action has completed, e.g once the drink
# is dispensed. The prompt should show again to serve the next customer.

# 2. Turn off the Coffee Machine by entering 'off' to the prompt
# a. for maintainers of the coffee machine, they can use 'off' as the secret word to turn off
# the machine. Your code should end execution when this happens

# 3. Print report
# a. When the user enters 'report' to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# 4. Check resources sufficeient?
# a. Whent the user chooses a drink, the program should check if there are enough
# resources to make that drink
# b. E.g. if Latte requires 200ml water but there is only 100ml left inthe machine. It should 
# not continue to make the drink but print: 'Sorry there is not enough water.'
# c. The same should happen if another resource is depleted, e.g. milk or coffee

# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies
# = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the 
# program should say 'Sorry that's not enough money. Money refunded.'
# b. But if the user has inserted enough money, then the cost of the drink gets added to the machine
# as the profit and this will be reflected the next time 'report' is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# 7. Make Coffee"""


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }



# """
# 1. Prompt user by asking 'What would you like? (expresso/latte/cappuccino):
# a. Check the user's input to decide what to do next.
# b. The prompt should show every time action has completed, e.g once the drink
# is dispensed. The prompt should show again to serve the next customer.
# """
# profit = 0
# is_on = True

# """function: is_resource_sufficient"""
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient"""
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# """function: process_coins"""
# def process_coins():
#     """Returns the total calculated from coins inserted"""
#     print("Please insert coins.")
#     total = int(input("How many quarters?: ")) * 0.25
#     total += int(input("How many dimes?: ")) * 0.1
#     total += int(input("How many nickles?: ")) * 0.05
#     total += int(input("How many pennies?: ")) * 0.01


# """function: transaction"""
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     global profit
#     money_received = 0.0
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False

# """function: make_coffee"""
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources"""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#         print(f"Here is your {drink_name} ☕️")

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")

#     else:
#         """we access a keyname using square bracket"""
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)