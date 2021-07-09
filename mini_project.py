# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
Choice=["Rock","Paper","Scissor"]
while True:
    print("WELCOME!")
    user_count=0
    comp_count=0
    for i in range(1,4):
        print("Round-",i)
        print("Enter a value:Rock=1,Paper=2,Scissor=3")
        your_choice=int(input())
        
        if (your_choice==1):
            print("Your Choice is Rock")
        elif (your_choice==2):
            print("Your Choice is Paper")
        elif (your_choice==3):
            print("Your Choice is Scissor")
        else:
            print("Wrong Choice Please Try Again")
        
        computerChoice=random.choice(Choice)
        print("Computer Selects",computerChoice)
        
        if your_choice==computerChoice:
            print("Draw")
        elif (your_choice=="Paper" and computerChoice=="Rock")or(
                your_choice=="Rock" and computerChoice=="Scissor") or(
                    your_choice=="Scissor" and computerChoice=="Paper"):
               user_count=user_count+1
        elif (your_choice=="Rock" and computerChoice=="Paper")or(
                 your_choice=="Scissor" and computerChoice=="Rock") or(
                     your_choice=="Paper" and computerChoice=="Scissor"): 
               comp_count=comp_count+1
    if (user_count>comp_count):
            print("You Win")
    elif(user_count<comp_count):
            print("Computer Wins")
    else:
            print("Draw")
    print("Do you want to play again Yes or No")
    x=input("enter Yes or No")
    if (x=='Yes' or x=='yes' or x=='YES'):
            continue
    else:
            break