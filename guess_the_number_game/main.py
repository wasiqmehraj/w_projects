
import random
from artista import logo
def guess_game():
    c_num=random.randint(0,100)
    level=input('What level do you want to play?\nE for Easy\nH for Hard.\n').lower()
    win=0
    if level=='h':
        chances=5
        print('You chose the hard level.\Lives=5')
    else:
        chances=10
        print('You chose the easy level.\Lives=10')
    while chances>0:
        user_guess=int(input('What is your Guess?'))
        if user_guess==c_num:
            print('You got the number correctly!!')
            win=1
            return win
        elif user_guess<c_num:
            print('Your guess is too Low.')
            
        elif user_guess>c_num:
            print('Your guess is too high.')
            
        chances-=1
        print(f'The number of chances left are {chances}.')
        
    return win


again='y'
while again=='y':
    print(logo)
    win=guess_game()
    if win==1:
        print('You won!')
    else:
        print('You exhaused all your chances.\nYou lost!')
    again=input('Do you want to play again? y or n\n')

print('Thanks for playing this awesome game!!')
    
        
            

    
    