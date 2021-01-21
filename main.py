from menu import MENU, resources

espresso = MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]

total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
total_money = 0


def user_choose(input_coffee):
    global total_coffee, total_milk, total_water
    water_needed = MENU[input_coffee]['ingredients']['water']
    milk_needed = MENU[input_coffee]['ingredients']['milk']
    coffee_needed = MENU[input_coffee]['ingredients']['coffee']

    if total_water < water_needed or total_coffee < coffee_needed or total_milk < milk_needed:
        print("Resource is not enough")
    else:
        total_water -= water_needed
        total_coffee -= coffee_needed
        total_milk -= milk_needed


def tank():
    global total_water, total_coffee, total_milk
    print(f'''
            Water: {total_water} 
            Coffee: {total_coffee} 
            Milk: {total_milk}
            Money: ${total_money}
            ''')
    refill = input("Refill? y/n ")
    if refill == "y":
        total_water = resources["water"]
        total_milk = resources["milk"]
        total_coffee = resources["coffee"]


def pay(item):
    global total_money
    user_penny = int(input("How much penny? "))
    user_nickel = int(input("How much nickel? "))
    user_dime = int(input("How much dime? "))
    user_quarter = int(input("How much quarter? "))
    user_penny *= 0.01
    user_nickel *= 0.05
    user_dime *= 0.10
    user_quarter *= 0.25
    user_money = user_penny + user_nickel + user_dime + user_quarter
    if item == "espresso":
        prices = espresso["cost"]
        if user_money >= prices:
            user_money -= prices
            print(f"Here is your {item}")
            print(f"Changes ${round(user_money)}")
            total_money += prices
        else:
            print("Not enough to buy this coffee")
    elif item == "latte":
        prices = latte["cost"]
        if user_money >= prices:
            user_money -= prices
            print(f"Here is your {item}")
            print(f"Changes ${round(user_money)}")
            total_money += prices
        else:
            print("Not enough to buy this coffee")
    elif item == "cappuccino":
        prices = cappuccino["cost"]
        if user_money >= prices:
            user_money -= prices
            print(f"Here is your {item}")
            print(f"Changes ${round(user_money)}")
            total_money += prices
        else:
            print("Not enough to buy this coffee")


def machine():
    is_worked = True
    while is_worked:
        display_menu = input('''
        Welcome to Coffee Machine
        What would you like?
        1. Espresso $1.50
        2. Latte $2.50
        3. Cappuccino $3.00
        ''')
        if display_menu == "espresso" or display_menu == "1":
            user_choose("espresso")
            pay("espresso")
        elif display_menu == "latte" or display_menu == "2":
            user_choose("latte")
            pay("latte")
        elif display_menu == "cappuccino" or display_menu == "3":
            user_choose("cappuccino")
            pay("cappuccino")
        elif display_menu == "off":
            is_worked = False
        elif display_menu == "result":
            tank()
        else:
            print("Error")


machine()
