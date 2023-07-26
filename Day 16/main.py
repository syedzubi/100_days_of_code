from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_coffee(coffee_choice, resources):
    if resources['coffee'] > MENU[coffee_choice]['ingredients']['coffee']:
        return True
    else:
        print("Not Enough Coffee , please kindly stock up")
def enough_water(coffee_choice, resources):
    if resources['water'] > MENU[coffee_choice]['ingredients']['water']:
        return True
    else:
        print(f"Not Enough Water , please kindly stock up")
def enough_milk(coffee_choice, resources):
    if resources['milk'] > MENU[coffee_choice]['ingredients']['milk']:
        return True
    else:
        print(f"Not Enough Milk , please kindly stock up")
def ingredients_sufficient(coffee_choice, resources):
    coffee_quantity = enough_coffee(coffee_choice, resources)
    water_quantity = enough_water(coffee_choice, resources)
    if coffee_choice == 'espresso':
        return coffee_quantity and water_quantity
    elif coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        return coffee_quantity and water_quantity and enough_milk(coffee_choice, resources)
def total_money():
    money_value = {'quarters': 0.25, 'Dimes': 0.10, 'Nickles': 0.05, 'Pennies': 0.01}
    input_quarters=int(input("how many quarters?: "))
    input_dimes=int(input("how many dimes?: "))
    input_nickles=int(input("how many nickles?: "))
    input_pennies=int(input("how many pennies?: "))
    total_amount = input_quarters*money_value['quarters'] + input_dimes*money_value['Dimes'] + \
                   input_nickles * money_value['Nickles'] + input_pennies*money_value['Pennies']
    return total_amount
def money_sufficient(coffee_choice, total_amount):
    beverage_cost = MENU[coffee_choice]['cost']
    if coffee_choice == 'espresso' and total_amount > beverage_cost:
        return True
    elif coffee_choice == 'latte' and total_amount > beverage_cost:
        return True
    elif coffee_choice == 'cappuccino' and total_amount > beverage_cost:
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
def any_refund(total_amount, coffee_choice):
    beverage_cost = MENU[coffee_choice]['cost']
    refund_amount = total_amount - beverage_cost
    if total_amount > beverage_cost:
        print(f"Here is ${round(refund_amount,2)} in change.")
    resources['money'] += beverage_cost
def reduce_resources(coffee_choice, resources):
    resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    if coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']

    return resources
def make_coffee(coffee_choice,resources):

    if ingredients_sufficient(coffee_choice, resources):
        total_amount = total_money()
        any_refund(total_amount, coffee_choice)
        if money_sufficient(coffee_choice, total_amount):
            reduce_resources(coffee_choice, resources)
            print(f"Here is your {coffee_choice} ☕. Enjoy!")

is_on = True
resources['money'] = 0
while is_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == 'off':
        is_on = False
    elif coffee_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gms")
        print(f"Money: ${resources['money']}")
    else:
        make_coffee(coffee_choice, resources)
