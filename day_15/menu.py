MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
    },
    "cost":1.5,
    },

    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },

    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.8,
    },

}  
profit = 0
resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"sorry there is not enough{item}")
           is_enough = False
    return is_enough


def process_coin():
    print("please insert coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.25
    total += int(input("how many nickles?: ")) * 0.25
    total += int(input("how many pennies?: ")) * 0.25
    return total

def is_transaction_successful(money_receive, drink_cost):
    if money_receive >= drink_cost:
        change = round(money_receive - drink_cost, 2)
        print(f"here is {change}$ in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money, money refunded")
        return False



def make_coffee(drink_name, order_ingredient):

    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here in your drink {drink_name} ")


is_on = True
while is_on:
    choice = input("what would you like?(espresso/latte/cappuccino): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"money:{profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment =  process_coin()
           is_transaction_successful(payment, drink["cost"])
        make_coffee(choice, drink["ingredients"])



