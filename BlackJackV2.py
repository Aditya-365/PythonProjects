import random

def Black_Jack() :
    Y_r1 = random.randint(1,11)
    Y_r2 = random.randint(1,11)
    Your_cards = [Y_r1, Y_r2]
    print(f"Your cards : {Your_cards} ")

    C_r1 = random.randint(1,11)
    C_r2 = random.randint(1,11)
    Computer_cards = [C_r1, C_r2]
    C_total = C_r1 + C_r2
    print(f"Computer's cards : [{C_r1},'?'] ")

    extra_card = input("Do you want extra cards (y/n) : ").lower()
    if extra_card == 'y' :
        Y_r3 = random.randint(1,11)
        print(f"You got {Y_r3}.")
        Y_total = Y_r1 + Y_r2 + Y_r3
        print(f"Your total is {Y_total}.")
    else :
        Y_total = Y_r1 + Y_r2
        print(f"Your total cards is {Y_total}. ")
    
    print(f"The computer's cards are [{C_r1},{C_r2}]")
    print(f"The computer's total is {C_total}")

    if Y_total > C_total :
        print("You Win.")
    else :
        print("You Lose.")


ans = 'y'
while ans == 'y' :
    Black_Jack() 
    ans = input("Do you want to play again(y/n) : ").lower()  