# Choose Your Own Adventure Application 

# Imported Modules
from src import number_guess
import random

# Instructions 
print('*********************************************************************************************')
print('Welcome!')
print('The instructions are simple.')
print('A mysterious creature has transported you to a remote outpost station in Space.')
print('You don\'t recognise the stars or planets, but outside you see a rainbow of colours that take your breath away, you must be in a stellar nursery.')
print('Along the way the mysterious creature will ask you questions, also you may encounter some challenges and puzzles to test your skills and knowledge!')
print('To wake up from this strange dream, if it even is a dream, type in quit() at any time.\n')

# Introduce quit functionality 
    
    # if input_value == "\quit":
    #     raise KeyboardInterrupt
    
    #     return input_value


# Are you ready to begin Control Flow
start_adventure = input("Are you ready for your journey? (Yes/No):\n").lower()

while True:
    if start_adventure == "yes" or start_adventure == "y":
        print('Lets begin!\n')

    
# Main Story - Asks Traveller Name

        print("Welcome Space Traveller")
        print("I have brought you here as we are in grave danger and I need your help!")
        print("You look around and realise you have been transported to the distant future where everything looks strange and computerised.")
        print("The mysterious creature is looking at you and asks.")
        traveller_name = input("What shall I call you?\n")
        print(f"Ah excellent, it is a bit hard for me to say this, but I will call you {traveller_name}!\n")
        print(f"The mysterious creature points ahead of you and says, '{traveller_name}, we need to go that way.'")

# Loops Story A, Story B and Story C

        challenge_one = input("Except you hear something coming. Ahead of you is a door, right next to you is a loose panel, or do you make a run for it? What do you do? Type: (door) / (hide) or (run)\n").lower().strip()
        if challenge_one == "run":
            print("\nYou take off running!\nOnce you turn the corner you press yourself against the metal walls listening carefully for any noise.\n")
            challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you trust it and pick it up? Type: (Yes) / (No)\n").lower().strip()
            if challenge_two == "no" or challenge_two == "n":
                print(f"\nOh hell no you say! Your mysterious friend smiles at you wisely and says, '{traveller_name}, a wise decision, they can bite your hand off!'./n")
                challenge_three = input(f"'{traveller_name}, we really must go, but before we can we need to get past the creature. Should we feed this creature.' Type: (Yes) / (No)/n").lower().strip()
                if challenge_three == "yes" or challenge_three == "y":
                    print("Good idea, lets feed it.")
                    choose_container = int(input("You see two containers near it. Which container do you feed it? The one labelled 0 or 1? Enter a number (0) or (1):\n"))
                    random_bottle = random.randint(0, 1)
                    if random_bottle == 0:
                        print("You open the container and throw the food at it. Look! Its eating!")
                        print(f"Your mysterious friend looks at you and then says, '{traveller_name}, THANK YOU!' As it picks up the fluffy creature./nYour mysterious friend continues to say, 'I am unable to touch these containers and needed help your to feed Nog here./nLet me take you back home!'")
                        print("Next thing you remember is waking up in your own bed. Was that all a dream?")
                    else:
                        print("Oh no... I don't think that was the right one, as the last thing you see is the fluffy creature lunging for your face!\nYou DEAD.")
                elif challenge_three == "no":
                    print("That was a bad mistake! As you try to leave the fluffy creature lunges for your face. The last thing you remember is the immeense pain.\nYou DEAD.")
                else:
                    print("What just happened?\nYou DEAD.")    
            elif challenge_two == "yes" or challenge_two == "y":
                print("\nAww how cute you think to youself.\nAs you reach out with your hand you see this giant mouth open wide with razor sharp teeth!\nIn an instance your arm is bitten off and you pass out from blood loss.\nYou DEAD!")
            else:
                print("What just happened?\nYou DEAD.")
        elif challenge_one == "hide":
            print("\nYou sqeeze into the tight space, quickly covering the panel back into place.\nNext minute you hear a thump on the panel as it opens to reveal the mysterious creature looking at you.")
            challenge_four = input(f"'It's safe {traveller_name}'. Do you leave your hiding spot? Type: (Yes) / (No)\n").lower().strip()
            if challenge_four == "yes" or challenge_four == "y":
                print("\nFollow me, I found somehing I want to show you.")
                print("The mysterious creature shows you a small metalic box, with etchings and a keypad on it.\nYou see the first letter as an 'S' and the last letter as a 'E'.")
                def check_password():
                    password = "space"
                    while input("What do you think the password could be? Enter your guess to see if it works:\n").lower().strip() != password:
                        print("You hear a loud noise with a mechanical voice repeating, 'Error, Error, Error'/nTry again\n")
                    print("\nYou hear a click and a whir of noises as the box opens to display a minuture galaxy.")
                    print(f"'{traveller_name}, you foud it! I was looking for my home world and here it is. You SAVED my World!")
                    print("A blinding flash of light errupts and you pass out. Only to wake up in your backyard under a sky full of stars.")
                    print("THE END")
                check_password()
            elif challenge_four == "no" or challenge_four == "n":
                print("\nYou look back at the mysterious creature and shake your head\nThe mysterious creature looks sad but puts the panel back.")
                print("As the panel is locked into place you realise there is no air in this tight space.\nYou pass out from lack of oxygen.\nYou DEAD.")
            else: 
                print("You start shaking uncontrollably. What is going on you think as your body heats up to a burning fury!\nYou DEAD.")
        else:
            print("\nYou push the door to reveal a room full of poisionous plants!\nYou accidentally brushed against one in your haste and start to feel sick. On no... you start to swell up!\n")
            guess = number_guess("Looking around you, you see three bottles of gooey liquid. One of them must be the antidote!\nQuick, which bottle do you choose? Guess ANY number or letter: \n")
            print(f"You quickly grab the bottle with the label, {guess} on it and drink it!\nOn no... you don't feel so good now...\nLast thing you hear is, {traveller_name}, that wasn't antidote!\nYou DEAD.")
        break

    else: 
        print('Maybe next time.!')
        break


  

 