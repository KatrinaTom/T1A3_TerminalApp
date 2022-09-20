# Choose Your Own Adventure Application 

# Imported Modules
from src import number_guess
import random
from sys import argv
import clearing
# from src import restart_game

def main():
# Instructions 
    print("*******************************************************************************")
    print("Welcome!")
    print("The instructions are simple.")
    print("An alien creature has transported you to a remote outpost station in Space.")
    print("You don\'t recognise the stars or planets.")
    print("Outside a window you see a rainbow of colours that take your breath away, you must be in a stellar nursery.")
    print("Along the way the alien creature will ask you questions.")
    print("you may even encounter some challenging puzzles to test your skills!")
    print("To wake up from this strange dream, if it even is a dream, close the Terminal Application at any time.\n")



    # Are you ready to begin Control Flow
    start_adventure = input("Are you ready for your journey? (Yes/No):\n").lower()

    while True:
        if start_adventure == "yes" or start_adventure == "y":
            print('Lets begin!\n')
            clearing.clear()

    # Main Story - Asks Traveller Name

            print("Welcome Space Traveller")
            print("I have brought you here as we are in grave danger and I need your help!")
            print("You look around and realise you have been transported to the distant future.")
            print("The alien creature is looking at you and asks.")
            traveller_name = input("What shall I call you?\n")
            print(f"\nIt is a bit hard for me to say this, but I will call you {traveller_name}!")
            print(f"Then the alien creature points ahead of you and says, '{traveller_name}, we need to go that way.'")

    # Loops Story A, Story B and Story C
            
            challenge_one = input("\nExcept you hear something coming....\nAhead of you is a door, a loose panel, or do you make a run for it?\nWhat do you do? Type: (door) / (hide) or (run)\n").lower().strip()
            clearing.clear()
            if challenge_one == "run":
                print("You take off running!\nYou turn the corner pressing yourself against the metal walls listening carefully for any noise.\n")
                challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you pick it up? Type: (Yes) / (No)\n").lower().strip()
                if challenge_two == "no" or challenge_two == "n":
                    print("\nNow way! Your alien friend smiles at you wisely.")
                    print(f"Saying, '{traveller_name}, a wise decision, they can bite your hand off!'.")
                    print("Before we can go we need to get past the creature, says the alien.")
                    challenge_three = input("Should we feed it?' Type: (Yes) / (No)\n").lower().strip()
                    if challenge_three == "yes" or challenge_three == "y":
                        print("\nGood thinking, lets feed it from one of those containers.")
                        random_bottle = int(input("Which container do you feed it? The one labelled 0 or 1? Enter a number (0) or (1):\n"))
                        random_bottle = random.randint(0, 1)
                        if random_bottle == 0:
                            print("\nYou open the container and throw the food at it. Look! Its eating!")
                            print(f"Your alien friend looks at you and then says, '{traveller_name}, THANK YOU!'")
                            print("The alien friend picks up the fluffy creature and says,")
                            print("'I am unable to touch these containers and needed help your to feed Nog!")
                            print("Next thing you remember is waking up in your own bed. Was that all a dream?")
                            print("THE END")
                            restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                            clearing.clear()
                            if restart == "yes" or restart == "y":
                                main()
                            else: 
                                print("Maybe next time.")
                                exit()
                            break
                        else:
                            print("Oh no... I don't think that was the right one.")
                            print("The last thing you see is the fluffy creature lunging for your face!\nYou DEAD.")
                            restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                            clearing.clear()
                            if restart == "yes" or restart == "y":
                                main()
                            else: 
                                print("Maybe next time.")
                                exit()
                            break
                    elif challenge_three == "no":
                        print("That was a bad mistake! As you try to leave the fluffy creature lunges for your face. The last thing you remember is the immeense pain.\nYou DEAD.")
                    else:
                        print("What just happened?\nYou DEAD.")    
                        restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                        clearing.clear()
                        if restart == "yes" or restart == "y":
                            main()
                        else: 
                            print("Maybe next time.")
                            exit()
                        break
                elif challenge_two == "yes" or challenge_two == "y":
                    print("\nAww how cute you think to yourself.\nYou reach out with your hand and see a giant mouth open wide with razor sharp teeth!\nIn an instance your arm is bitten off and you pass out from blood loss.\nYou DEAD!")
                else:
                    print("What just happened?\nYou DEAD.")
                    restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                    clearing.clear()
                    if restart == "yes" or restart == "y":
                        main()
                    else: 
                        print("Maybe next time.")
                        exit()
                    break
            elif challenge_one == "hide":
                print("You sqeeze into the tight space, quickly covering the panel back into place.\nNext minute you hear a thump on the panel as it opens to reveal the alien creature looking at you.")
                challenge_four = input(f"'It's safe {traveller_name}'. Do you leave your hiding spot? Type: (Yes) / (No)\n").lower().strip()
                if challenge_four == "yes" or challenge_four == "y":
                    print("\nFollow me, I found somehing I want to show you.")
                    print("\n\nThe alien creature shows you a small metallic box, with etchings and a keypad on it.\nWhat do you think the password could be?")
                    def check_password():
                        password = "space"
                        while input("You see the first letter as an 'S' and the last letter as a 'E'. Enter your guess to see if it works:\n").lower().strip() != password:
                            print("\n\nYou hear a loud noise with a mechanical voice repeating, 'Error, Error, Error'\nYou try again.\n")
                        print("\nYou hear a click and a whir of noises as the box opens to display a minuture galaxy.")
                        print(f"'{traveller_name}, you found it! I was looking for my home world and here it is. You SAVED my World!")
                        print("A blinding flash of light errupts and you pass out. Only to wake up in your backyard under a sky full of stars.")
                        print("THE END")
                        restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                        clearing.clear()
                        if restart == "yes" or restart == "y":
                            main()
                        else: 
                            print("Maybe next time.")
                            exit()
                    check_password()
                elif challenge_four == "no" or challenge_four == "n":
                    print("\nYou look back at the alien creature and shake your head!\nThe alien creature looks sad but puts the panel back.")
                    print("As the panel is locked into place you realise there is no air in this tight space.\nYou pass out from lack of oxygen.\nYou DEAD.")
                    restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                    clearing.clear()
                    if restart == "yes" or restart == "y":
                        main()
                    else: 
                        print("Maybe next time.")
                        exit()
                    break
                else: 
                    print("You start shaking uncontrollably. What is going on you think as your body heats up to a burning fury!\nYou DEAD.")
                    restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                    clearing.clear()
                    if restart == "yes" or restart == "y":
                        main()
                    else: 
                        print("Maybe next time.")
                        exit()
                    break
            else:
                print("You push the door to reveal a room full of poisionous plants!\nYou accidentally brushed against one in your haste and start to feel sick.\nOn no... you start to swell up!\n")
                print("Looking around you, you see three bottles of gooey liquid. One of them must be the antidote!\n")
                guess = number_guess("Quick!, which bottle do you choose? Guess ANY number or letter: \n")
                print(f"You quickly grab the bottle with the label, {guess} on it and drink it!")
                print("On no... you don't feel so good...")
                print(f"Last thing you hear is, {traveller_name}, that wasn't antidote!")
                print("You DEAD.")
                restart=input("Do you want to play again? Type: (Yes) / (No)\n").lower().strip()
                clearing.clear()
                if restart == "yes" or restart == "y":
                    main()
                else: 
                    print("Maybe next time.")
                    exit()
                break

        else: 
            print('Maybe next time.')
            break

main()


  

 