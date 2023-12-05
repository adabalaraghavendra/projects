from random import randint
easy_level=10
hard_level=5
def cheak(answer,guess,turns):
    if guess > answer:
        print("to high")
        return turns-1
    elif guess<answer:
        print("To low")
        return turns-1
    else:
        print(f"you got it.the answer is {answer}")
def select():
    level=input("choose a difficulty.Type 'easy' or 'hard'")
    if level=='easy':
        return easy_level
    else:
        return hard_level
def game():
    print("welcome to number guessing game")
    print("nuimber between 1 and 100")
    answer=randint(1,100)
    print(f"currect answer is {answer}")
    turns=select()
    guess=0
    while guess!=answer:
        print(f"the no of turns remaining is {turns}")
        guess=int(input("make a guess:"))
        turns=cheak(answer,guess,turns)
        if turns==0:
            print("You lose game")
            return
        elif guess!=answer:
            print("guess again")
game()

