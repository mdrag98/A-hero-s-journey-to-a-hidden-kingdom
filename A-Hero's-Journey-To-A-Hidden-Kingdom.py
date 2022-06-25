import sys
import random
from time import sleep
wolf = r'''                     .
                    / V\
                  / `  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |
  ________|   _/_  | |
<__________\______)\__)'''
r=0

#This function i have used to essentially "clear" the terminal by just entering a new line 50 times
def ClearAll():
    sys.stdout.write("\n" *50)
#This function initiates the story, printing to the user the introduction and what they should expect
#The function will be called later in the code
# instead of compiling my write statements all to one line of code, ive added a delay between each line to give a more satisfying effect
def adventureSTART():
    sys.stdout.write("The story begins with our hero "+Hero+"A young adventurer living in a small village who recently turned "+HeroAge)
    sleep(1)
    sys.stdout.write("On their birthday being told by their mother that they are now of age to leave the village and set out on their journey to adulthood")
    sleep(1)
    sys.stdout.write("\nOn this journey they are expected to overcome obstacles and challenges set before them, their mother gave them a bag full of essentials and directed them to the door to set them on their way")
    adventureSteal()


def adventureSteal():
    sleep(1)
    sys.stdout.write("\n\nOur hero has set out on their journey and headed north of the town, after a few hours of travel the hero stumbles across a picnic blanket with some food and drink sprawled upon it")
    sleep(1)
    sys.stdout.write("\n Our hero feels their stomach rumble in hunger and thinks to themself that the food looks really tasty, will our hero steal some for themself?\n")
    #Takes the user input and changes the outcome based on their response
    #I use input here as an alternative of "sys.stdin.readline" as no matter how much i tried i could not figure out how to get it to work with that line instead
    #the code block will continuesly loop untill the user inputs a valid yes or no response
    while True:
        ans = input(" yes or no? ")
        while r ==0:
            if ans == "yes":
                adventureNaugty()
                sleep(5)
                sys.stdout.write("-------------------end------------------\n\n\n")
    #The user has stolen something that is not theres, to teach the child that this is not something they should be doing this has caused them to fail the adventure
                adventureSTART()
            elif ans == "no":
                adventureCont()
            else:
                ans = input("\n please enter yes or no:  ")
            continue
                
#This function is for whenever the user does something that would get them in trouble, e.g stealing, hurting someone or breaking the law
#this way i can call it when they do something of this nature so i dont have to re write the code each time
def adventureNaugty():
    sys.stdout.write("A stranger spots you and recognizes you as his neighbour, he see's you doing something you shouldnt and imidiately calls your mother, she comes and gets you and takes you home, you are now grounded forever")

def adventureCont():
    sys.stdout.write("\nYou see something that doesnt belong to you and decide to leave it be, stealing is bad and you rightfully avoid doing so")
    sleep(2)
    sys.stdout.write("\nYou remember you have snacks in your bag and have some of those instead, then moving along into a forest ruled by "+str(Villain)+" that has been untouched for " +str(VillAge)+" years")
    sleep(2.5)
    sys.stdout.write("\nupon entering the forest you hear quiet rumbling, you move close to the noise and see its a large doglike creature, possibly a wolf")
    sleep(2.5)
    adventureWolf()

def adventureWolf():
    sys.stdout.write("\nDo you approach the creature and attempt to pet it or do you move on?:\n")
    response=input("pet or move on: ")
    while r ==0:
        if response == "pet":
            adventureWolfCont()
            adventureNaugty()
            sleep(5)
            sys.stdout.write("\nDont approach wild animals, they are dangerous and can hurt you")
            sys.stdout.write("\n------------------------------end-------------------------------\n\n\n\n\n")
            sleep(4)
            adventureSTART()
        elif response == "move on":
            adventureEnd()
        else:
            response = input("\n please input pet or move on:  ")
        continue
#The function i made prior clears the terminal and then the user gets displayed a ascii art of a wolf before being cleared again
def adventureWolfCont():
    ClearAll()
    sys.stdout.write(wolf)
    sleep(1)
    sys.stdout.write("\nThe wolf howls agressively and attacks you")
    sleep(7)
    ClearAll()

def adventureEnd():
    sys.stdout.write("\nYou quickly move on through the forest trying to reach the other side\n")
    sleep(3)
    sys.stdout.write("You see a break in the trees, between which a bright light, you approach it as fast as you can\n")
    sleep(3)
    sys.stdout.write("Upon getting to the break you start to see a building, you exit the forest and see that it is a large castle\n")
    sleep(2)
    sys.stdout.write("Broken down and seemingly ancient, is this the magical castle you heard stories about as a child?\n")
    sleep(2)
    sys.stdout.write("---------------------------------------End of chapter 1------------------------------------------")

#Gathering input from the user to help create the narative by having them name the main hero and villain 
# as well as their age wich will help with calculations later
sys.stdout.write("Enter Hero Name:\n")
Hero = sys.stdin.readline()
sys.stdout.write("Enter the Hero's Age:\n")
HeroAge = sys.stdin.readline()
sys.stdout.write("\n Enter Name of the villain: \n")
Villain = sys.stdin.readline()
sys.stdout.write("Enter Age of the villain: \n")
VillAge = sys.stdin.readline()

adventureSTART()




