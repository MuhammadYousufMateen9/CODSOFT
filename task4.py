import random
elements=['r','p','s']
rounds=0
user_won=0
computer_won=0
tied=0
print('''\nCarefully read the instructions first then start the game. Have fun and enjoy.\n
\033[93mINSTRUCTIONS !!!\033[0m\n
    1) Start the game by selecting either rock, paper or scissor.\n
    2) The computer will randomly choose rock, paper or scissor.\n
    3) The winning criteria will be :
        - Rock beat Scissor
        - Scissor beats Paper
        - Paper beat Rock\n
    4) You can write 'r' for rock, 'p' for paper and 's' for scissor.''')

print()
while True:
    rounds+=1
    print(f'\033[92m\nROUND {rounds}\033[0m')
    while True:
        user_choice=input('Enter your choice (r, p or s) : ').lower()
        if user_choice=='r' or user_choice=='p' or user_choice=='s':
            break
        else:
            print("\033[91mError: Your choice must be 'r' for rock, 'p' for paper or 's' for scissor.\033[0m")
            continue
    while True:
        computer_choice=random.choice(elements)
        print(f"Computer's Choice : {computer_choice}")
        if user_choice==computer_choice:
            print('Tied')
            tied+=1
            break
        elif (user_choice=='r' and computer_choice=='s') or (user_choice=='p' and computer_choice=='r') or (user_choice=='s' and computer_choice=='p'):
            print('You Won :)')
            user_won+=1
            break
        elif (user_choice=='s' and computer_choice=='r') or (user_choice=='r' and computer_choice=='p') or (user_choice=='p' and computer_choice=='s'):
            print('You Loose :(')
            computer_won+=1
            break
    while True:
        continue_ask=input('\nWant to play again (y/n) : ').lower()
        if continue_ask=='y':
            break
        elif continue_ask=='n':
            break
        else:
            print("\033[91mError: Choose 'y' to continue or 'n' for exit.\033[0m")
            continue
    if continue_ask=='y':
        continue
    break
print(f'''\033[92m\nRESULTS !\033[0m
\nTotal {rounds} rounds played.\n
You have won {user_won} rounds.\n
Computer have won {computer_won} rounds.\n
And {tied} rounds are tied.''')