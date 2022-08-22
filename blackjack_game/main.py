import random
from art import logo
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
def get_card(cards):
    got_card=cards[random.randint(0,13)]
    return got_card
def get_input():
    decide=input('Do you want to STAND or HIT? S or H?').lower()
    return decide
def ace_adjust(hand_list):
    if sum(hand_list)>21:
        i=0
        while i<=len(hand_list)-1:
            if hand_list[i]==11:
                hand_list[i]=1
            i+=1
    return hand_list

def start_blackjack(cards):
    comp_hand_1=get_card(cards)
    comp_hand_2=get_card(cards)
    com_list=[comp_hand_1,comp_hand_2]
    adj_comp_list=ace_adjust(com_list)
    print(f"Computer's cards: \n [🃏,{adj_comp_list[0]}]")
    user_hand_1=get_card(cards)
    user_hand_2=get_card(cards)
    user_list=[user_hand_1,user_hand_2]
    adj_user_list=ace_adjust(user_list)
    print(f"Your cards are:\n {adj_user_list}.")
    start_list=[adj_comp_list, adj_user_list]
    return start_list

def real_game(cards,comp_list,user_list,starting,win):
    if starting==1:
        start_list=start_blackjack(cards)
        comp_list=start_list[0]
        user_list=start_list[1]

    if sum(user_list)==21:
        print('Won without even playing')
        win=1 
    else:
        user_input=get_input() #s--->stand and h--->hit
        if user_input=='s':
            
            if sum(comp_list)<17:
                while sum(comp_list)<17:
                    comp_list.append(get_card(cards))
                    comp_list=ace_adjust(comp_list)
                
            if sum(comp_list)==21:
                print('You Loose')
                win=0
            elif sum(comp_list)>21:
                print('You win, computer got busted!!')
                win=1
            elif sum(comp_list)>16 and sum(comp_list)<21:
                if sum(comp_list)>sum(user_list):
                    print('You lost, computer has more!')
                    win=0
                else:
                    print('You won, you have more than computer!!')
                    win=1
            
        elif user_input=='h':
            user_list.append(get_card(cards))
            if sum(user_list)<17:
                while sum(user_list)<17:
                    user_list.append(get_card(cards))
                    user_list=ace_adjust(user_list)
                                        
            if sum(user_list)==21:
                print('You got the blackjack, you won!!')
                win=1
            elif sum(user_list)>21:
                print('You got busted!!,you loose!!')
                win=0
            elif sum(user_list)>16 and sum(user_list)<21:
                starting=0
                real_game(cards,comp_list,user_list,starting,win=0)
    return win
                
   

#start
print(logo)
money_in_bank=int(input('For how much do you want to purchase the coins in wasiqs casino? \n$'))
if money_in_bank>0:
    orig_money=money_in_bank
    no_coin_first=0
else:
    no_coin_first=1
play='y'
while play=='y':
    if money_in_bank==0:
        print('You, my good sir are BANKRUPT!! You have no coins')
        play='n'
        break
    bet=int(input("How much will you bet? "))
    if bet>money_in_bank:
        print("You haven't purchsed enough coins for this bet.\nTry a smaller bet than this.")
        play='y'
    elif bet<=0:
        print('Invalid bet.\n Try with bet greater than 0')
    else:
        print("Wasiq's casino welcomes you!")
        win=real_game(cards,comp_list=[],user_list=[],starting=1,win=0)
        if win==1:
            money_in_bank+=bet
        elif win==0:
            money_in_bank-=bet
        print(f"You have {money_in_bank} worth of coins left")
        play=input('Do you want to play Blackjack again? y or n\n')
if no_coin_first==0:
    print(f"You came in here with ${orig_money}\nNow you have ${money_in_bank}. Your net earning is {(money_in_bank-orig_money)*100/orig_money}%")

else:
    print("Looks like you don't have money to buy coins in the first place. Bye!")