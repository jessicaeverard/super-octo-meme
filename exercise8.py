import random
import time

game = ["rock", "scissors", "paper"]
x = random.choice(game)

print ("rock, paper or scissors")
user = input()

if x == "rock":
    if user == "paper":
        print ("...")
        time.sleep(1)
        print (x)
        print ("you win")
    elif user == "scissors":
        print ("...")
        time.sleep(1)
        print (x)
        print ("computer wins :)")
    else:
        print ("...")
        time.sleep(1)
        print (x)
        print ("draw")

elif x == "paper":
    if user == "scissors":
        print ("...")
        time.sleep(1)
        print (x)
        print ("you win")
    elif user == "rock":
        print ("...")
        time.sleep(1)
        print (x)
        print ("computer wins :)")
    else:
        print ("...")
        time.sleep(1)
        print (x)
        print ("draw")

elif x == "scissors":
    if user == "rock":
        print ("...")
        time.sleep(1)
        print (x)
        print ("you win")
    elif user == "paper":
        print ("...")
        time.sleep(1)
        print (x)
        print ("computer wins :)")
    else:
        print ("...")
        time.sleep(1)
        print (x)
        print ("draw")

else:
    print ("idk")
    
