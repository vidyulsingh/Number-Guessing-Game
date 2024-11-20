import random

print()

print("Welcome to the nuumber guessing game!!")
print("Instructions :You have three chances to guess a random number between 0 and 10")

print()
print()


def play_game():

    random_number=random.randint(0,10)

    attempts=3
    usr_chances=0

    while usr_chances<attempts:
        usr_guess=int(input("Enter a guess:"))
        print()
        usr_chances+=1

        if usr_guess==random_number:
            print("Congrats!!, You Won")
            break
        else :
            print(f"You got it wrong, you have {attempts-usr_chances} more chances")
            print()

play_game()

replay=input("Do you want to play again(Y/n)")

if replay!='Y':
    exit()
else :
    play_game()