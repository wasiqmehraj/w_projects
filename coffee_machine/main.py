from coffee_details import menu
from coffee_details import resources

def ask_coins():
    quaters = float(input('Enter the number of quaters: '))*0.25
    dimes = float(input('Enter the number of dimes: '))*0.10
    nickels = float(input('Enter the number of nickels: '))*0.05
    pennies = float(input('Enter the number of pennies: '))*0.01
    in_money = quaters+dimes+nickels+pennies
    in_money = round(in_money,2)
    if in_money>0:
        print(f"You gave me ${in_money}")
        return in_money
    else:
        print('Entries invalid.\nTry again!')
        ask_coins()

def give_coins(in_money,cost):
    if cost > in_money:
        print("You don't have enough coins! Bye!")
        fail = 1
        out_money = 0
        outero = [fail, out_money]
        return outero
    else:
        fail = 0
        out_money = in_money-cost
        outero = [fail, out_money]
        return outero
def check_resouces(resources,choice):
    if resources["water"]>=menu[choice]["ingredients"]["water"] and resources["milk"]>=menu[choice]["ingredients"]["milk"]  and resources["coffee"]>=menu[choice]["ingredients"]["coffee"] :
        have_resources=1
        return have_resources
    else:
        have_resources=0
        return have_resources

def coffee_machine(resources):
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    cost = menu[choice]['cost']
    in_money=ask_coins()
    have_resources=check_resouces(resources,choice)
    if have_resources==1:
        if choice=='espresso' or choice=='latte' or choice=='cappuccino':
            outero=give_coins(in_money,cost)
            fail=outero[0]
            out_money=round(outero[1],2)
            if fail==0:
                print(f"Here is ${out_money} dollars in change.")
                print(f"Here is your {choice}☕")

        else:
            print(f'So Sorry!\nWe do not have {choice}. Select another one!')
            coffee_machine(resources)
            fail=1
    else:
        print('We do not have enough resources to give you the coffee, Come back later.')
        print(f'Here is your ${in_money} back. >>REFUND of ${in_money}<<')
        fail=1
    result=[resources,fail,choice]
    return result

again="y"
while again=='y':
    result = coffee_machine(resources)
    resources = result[0]
    fail = result[1]
    choice = result[2]
    if fail==0: # will count the resources
        resources["water"] -= menu[choice]['ingredients']["water"]
        resources["milk"] -= menu[choice]['ingredients']["milk"]
        resources["coffee"] -= menu[choice]['ingredients']["coffee"]

    elif fail==1: # wont count the resources
        print('Sorry for inconvenience')
    again=input("Do you want to use the coffee machine again? Y or N ").lower()
print("Thanks for using this coffee machine! \n Good bye!!")