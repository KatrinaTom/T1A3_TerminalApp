# Choose Your Own Adventure Application 

# Imported Modules
from functions import guess_number
import random
from sys import argv
import clearing
from story_line import instructions
from story_line import main_story
from ending import you_died
from ending import restart_game
from ending import finished_story
from pyfiglet import Figlet
from ascii import ascii_title

def main():

# Instructions 
    instructions()

    # Are you ready to play game -  Control Flow (77 Charaters)
    start = input("Are you ready for your journey? (Yes) / (No):\n").lower().strip()

    while True:
        if start == "y" or start == "yes":
            print("Lets Begin!")
            clearing.clear()

            ascii_title()
            main_story()

            # Ask for Traveller name - Be in the story
            traveller_name = input("What shall I call you?\n").strip()
            print(f"\nIt is hard to say, but I will call you {traveller_name}!")
            print(f"The alien creature points and says, '{traveller_name}, we must go.'")
            print("Except you hear something coming....\n")

            # Decision One (door) / (hide) / (run) 
            print("Ahead is a door, a loose panel, or do you run?")
            dec_one = input("What do you do? Type: (door) / (hide) or (run)\n").lower().strip()
            clearing.clear()

            # first decision
            if dec_one == "run":
                print("\nYou take off running!")
                print("Turning a corner you press yourself against a metal wall.")

                # Story C / 2nd Decision
                challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you pick it up? Type: (Yes) / (No)\n").lower().strip()
                if challenge_two == "no" or challenge_two == "n":
                    print("\nNow way! Your alien friend smiles at you wisely.")
                    print(f"Saying, '{traveller_name}, a wise decision, they can bite your hand off!'.")
                    print("Before we can go we need to get past the creature, says the alien.")

                    # Story C / 3rd Decicion
                    challenge_three = input("Should we feed it?' Type: (Yes) / (No)\n").lower().strip()
                    if challenge_three == "yes" or challenge_three == "y":
                        print("\nGood thinking, lets feed it from one of those containers.")

                        # Story C / First Test
                        random_bottle = int(input("Which container do you feed it? The one labelled 0 or 1? Enter a number (0) or (1):\n"))
                        random_bottle = random.randint(0, 1)
                        if random_bottle == 0:
                            print("\nYou open the container and throw the food at it. Look! Its eating!")
                            print(f"Your alien friend looks at you and then says, '{traveller_name}, THANK YOU!'")
                            print("The alien friend picks up the fluffy creature and says,")
                            print("'I am unable to touch these containers and needed help your to feed Nog!")
                            print("Next thing you remember is waking up in your own bed. Was that all a dream?")
                            finished_story()
                            restart_game()

                            # restart_game()
                            restart_game()
                            
                        else:
                            print("Oh no... I don't think that was the right one.")
                            print("The last thing you see is the fluffy creature lunging for your face!")
                            you_died()
                            
                            # restart_game()
                            restart_game()
                           
                    elif challenge_three == "no":
                        print("That was a bad mistake! As you try to leave the fluffy creature lunges for your face. The last thing you remember is the immeense pain.\n")
                        you_died()

                        # restart game
                        restart_game()

                    else:
                        print("What just happened?\n")    
                        you_died()
                        
                        # restart game
                        restart_game()

                elif challenge_two == "yes" or challenge_two == "y":
                    print("\nAww how cute you think to yourself.")
                    print("You reach out with your hand and see a giant mouth open wide with razor sharp teeth!")
                    print("In an instance your arm is bitten off and you pass out from blood loss.\n")
                    you_died()

                    # restart game
                    restart_game()

                else:
                    print("What just happened?\n")
                    you_died()
                    
                    # Restart function
                    restart_game()

            # Story B / Decision 1
            elif dec_one == "hide":
                print("\nYou sqeeze into the dark hole.")
                print("Covering the panel back into place...")
                print("After a few heartbeats, the alien creature opens the panel.")  

                # Decision
                challenge_four = input(f"'It's safe {traveller_name}'. Do you leave your hiding spot? Type: (Yes) / (No)\n").lower().strip()
                if challenge_four == "yes" or challenge_four == "y":
                    print("\nFollow me, I found somehing I want to show you.")
                    print("\n\nThe alien creature shows you a small metallic box, with etchings and a keypad on it.\nWhat do you think the password could be?")
                   
                    # Story B / Test                    
                    # Turn this into a function                   
                    correct_password = False
                    password = "space"
                    i = 0
                    while correct_password == False and i < 3:
                        attempted_password = input("You see the first letter as an 'S' and the last letter as a 'E'. Enter your guess to see if it works:\n").lower().strip()
                        if attempted_password == password:
                            print("It worked!")
                            correct_password = True
                        else:
                            i += 1 
                            print(f"\nYou hear a loud noise with a mechanical voice repeating, 'Error, Error, Error'\nTry Again! {3 - i} Attempts left.\n")
                    if correct_password == True:
                        print("\nYou hear a click and a whir of noises as the box opens to display a minuture galaxy.")
                        print(f"'{traveller_name}, you found it! I was looking for my home world and here it is. You SAVED my World!")
                        print("A blinding flash of light errupts and you pass out. Only to wake up in your backyard under a sky full of stars.")
                        finished_story()
                        restart_game()
                    else:
                        print("The box starts to shake in your hands and a loud noise errupts from it.\n")
                        you_died()
                    
                    # Restart function
                    restart_game()

                elif challenge_four == "no" or challenge_four == "n":
                    print("\nYou look back at the alien creature and shake your head!\nThe alien creature looks sad but puts the panel back.")
                    print("As the panel is locked into place you realise there is no air in this tight space.\nYou pass out from lack of oxygen.")
                    you_died()
                    
                    # Restart function
                    restart_game()

                else: 
                    print("You start shaking uncontrollably. What is going on you think as your body heats up to a burning fury!\n")
                    you_died()

                    # Restart function
                    restart_game()

            elif dec_one == "door":
                print("\nYou push the door to reveal a room full of poisionous plants!")
                print("You accidentally brushed against one and start to feel sick.")
                print("You see bottles of gooey liquid, one must be antidote!\n")        
            
                # Challenge 1, guess the bottle of antidote
                guess_number()
                print(f"Last thing you hear is, {traveller_name}, that wasn't antidote!")
                
                # End of Story - you died.
                you_died()

                # Restart function 
                restart_game()

            else:
                print("Something went wrong. You black out!")

                # Restart function 
                restart_game()

        elif start == "no" or start == "n":
            print("Thats too bad, maybe next time")
            break
        else:
            print("Are you sure you entered the right phrase?")   
            
            # Restart function 
            restart_game()

# Where the code starts
            
     
main()




  

 

  

 