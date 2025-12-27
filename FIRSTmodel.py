# PROJECT 1: SNAKE, WATER, GUN GAME

'''
Snake Water Gun or Rock Paper Scissors
so 
1 is for ROCK OR GUN
-1 is for PAPER OR WATER
0 is for SCISSORS OR SNAKE 

'''

import random
computer = random.choice([1, -1, 0])
youstr = input (" ENTER YOUR CHOICE : ")

youdict = {  "r" : 1 , "p" : 0, "s" : 0 }
reversedict = { 1 : "rock" , -1 : "paper" , 0 : "scissors"}
you = youdict[youstr]

# By now we have 2 number (variables), you and computer 

print( f" you choose {reversedict[you]} \n computer choose {reversedict[computer]}")

if (you == computer ):
    print (" THIS ROUND IS DRAW !")
else:
    if ((computer - you ) == -2 or (computer - you ) == 1):
     print(" YOU LOSE ! ")
    else :
     print(" YOU WIN ! ")

'''
  if (you == 1 or computer == -1 ): 
        print(" YOU LOSE !")
    
    elif(you == -1 or computer == 1 ): (you - computer) :  -2
        print(" YOU WIN ! ")
    elif(you == 0 or computer == -1 ): (you - computer) :  1
        print(" YOU WIN ! ")
    elif(you == -1 or computer == 1 ): (you - computer) : -2
        print(" YOU LOSE  ! ")
    elif(you == 1 or computer == 0 ): (you - computer) : 1
        print(" YOU WIN ! ")
    elif(you == 0 or computer == 1 ): (you - computer) : -1
        print(" YOU LOSE ! ")
    elif(you == -1 or computer == 0 ): (you - computer) : -1
        print(" YOU LOSE  ! ")
else :
   print(" SOMETHINK WENT WRONG ! ")

'''
