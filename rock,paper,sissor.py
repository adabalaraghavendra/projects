
import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
sessor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_codes=[rock,paper,sessor]
user_choice=int(input('enter input "rock"=0,"paper"=1,"sessor"=2\n'))
computer_choice=random.randint(0,2)
if(user_choice>=3 or user_choice<0):
    print("enter valid number")
else:
    print(game_codes[user_choice])
    print(game_codes[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("you wins")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif(computer_choice>user_choice):
        print("you lose")
    elif computer_choice==user_choice:
        print("its a draw")
    elif user_choice>computer_choice:
        print("you win")
    