import random


def play(level,limit,maximum):
    """a function to simulate a guessing game."""
    count = 1
    user_choice = 0
    answer = random.randint(1,maximum)
    while count <= limit:
        user_choice = int(input("Enter secret number: "))
        if user_choice == answer:
            print("you got it right")
            break
        else:
            print("you got it wrong")
            count += 1
            print(f"you have {limit-1} guesses left")
            continue
        if count == limit:
            print("Game over")
            break

print("Hello user, welcome to my guessing game. there are three levels in this game." + \
    "easy, medium and hard. so pick the one you wish to play")

level = input("Enter level: ")


if level == "easy":
    print("you have chosen the easy level. for this level, you have the chance to guess a number from 1 to 10. are you ready? es or no")
    response = input("")
    if response == "yes":
        play(level,6,10)
    else:
        print("it seems you're not ready. see you later")
elif level == "medium":
    print("you have chosen the mediu level. for this level, you have the chance to guess a number from 1 to 20. are you ready? es or no")
    response = input("")
    if response == "yes":
        play(level,4,20)
    else:
        print("it seems you're not ready. see you later")
elif level == "hard":
    print("you have chosen the hard level. for this level, you have the chance to guess a number from 1 to 50. are you ready? es or no")
    response = input("")
    if response == "yes":
        play(level,3,50)
    else:
        print("it seems you're not ready. see you later")
else:
    print("Enter a valid level")