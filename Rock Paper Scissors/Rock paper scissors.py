import random

def play():
    user = input("ROCK (R) - PAPER (P) - SCISSORS (S): ")
    computer = random.choice(['R','P','S'])

    print("User = ", user)
    print("Computer = ",computer)
    
    if user == computer:
        return "It's a tie"
    elif is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"

def is_win(player, opponent):
    if ((player == 'R') and (opponent == 'S')) or ((player == 'S') and (opponent == 'P')) or \
       ((player == 'P') and (opponent == 'R')):
        return True
    return False

while (True):
    start = input(" Do you wanna play RPS? (Y/N) ")
    if (start == "Y" or start == 'y'):
        print(play())
    else:
        break
        


        
    
