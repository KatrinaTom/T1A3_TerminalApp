# Choose Your Own Adventure Application 

# Imported Modules
from functions import guess_number, password_guess, random_contaner
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
            clearing.clear()
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
                print("Turning a corner you press yourself against a metal wall.\n")

                # Story A / 2nd Decision
                print("You see a small fluffy creature with big eyes.")
                dec_two = input("Do you pick it up? Type: (Yes) / (No)\n").lower().strip()
                clearing.clear()
                if dec_two == "no" or dec_two == "n":
                    print("\nNo way! Your alien friend smiles at you wisely.")
                    print(f"'A wise decision {traveller_name}, they can bite your hand off!.'")

                    # Story A / 3rd Decicion
                    print("You still need to get past the creature.")
                    dec_three = input("Should you feed it?' Type: (Yes) / (No)\n").lower().strip()
                    if dec_three == "yes" or dec_three == "y":
                        print("\nGood thinking, lets feed it from one of those containers.")

                        # Story A / First Challenge
                        random_contaner()
                        print("\nThe alien friend picks up the fluffy creature and says,")
                        print("'I am unable to touch these containers.'")
                        print("'I needed help your to feed my pet!'\n")
                        print("Next thing you remember is waking up in your own bed. Was that all a dream?")
                        
                        # Finished Story A
                        finished_story()

                        # Restart game 
                        restart_game()
                           
                    elif dec_three == "no":
                        print("\nThat was a bad mistake!")
                        print("You try to get past the creature, except it lunges at you!")
                        print("The last thing you remember is the immeense pain.")
                        you_died()

                        # Restart game
                        restart_game()

                    else:
                        print("What just happened?\n")    
                        you_died()
                        
                        # Restart game
                        restart_game()

                elif dec_two == "yes" or dec_two == "y":
                    print("\nAww how cute you think to yourself.")
                    print("You reach out with your hand.")
                    print("and see a giant mouth open wide with razor sharp teeth!")
                    print("Your arm is bitten off and you pass out from blood loss.\n")
                    you_died()

                    # Restart game
                    restart_game()

                else:
                    print("What just happened?\n")
                    you_died()
                    
                    # Restart game
                    restart_game()

            # Story B / Decision 1
            elif dec_one == "hide":
                print("\nYou sqeeze into the dark hole.")
                print("Covering the panel back into place...")
                print("After awhile, the alien creature opens the panel.\n")  

                # Story A - Decision
                print(f"'It's safe {traveller_name}.'")
                dec_four = input("Do you leave your hiding spot? Type: (Yes) / (No)\n").lower().strip()
                clearing.clear()
                if dec_four == "yes" or dec_four == "y":
                    print("Follow me, I found something I want to show you.")
                    print("\nThe alien creature shows you a small metallic box.")
                    print("It has familar etchings on it and a keypad.")
                    print("What do you think the password could be?")
                   
                    # Story B / Challenge, guess the password                    
                    password_guess()

                    # Finished story
                    finished_story()
                    
                    # Restart game
                    restart_game()

                elif dec_four == "no" or dec_four == "n":
                    print("\nYou look back at the alien creature and shake your head!")
                    print("The alien creature looks sad but puts the panel back.")
                    print("As the panel is locked into place.")
                    print("You realise there is no air in this tight space.")
                    print("You pass out from lack of oxygen.")
                    you_died()
                    
                    # Restart game
                    restart_game()

                else: 
                    print("You start shaking uncontrollably.")
                    print("Your body heats up to a burning fury!")
                    you_died()

                    # Restart game
                    restart_game()

            elif dec_one == "door":
                print("\nYou push the door to reveal a room full of poisonous plants!")
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
            print("Thats too bad, maybe next time.")
            break
        else:
            print("Are you sure you entered the right phrase?")   
            
            # Restart function 
            restart_game()

# Where the code starts   
main()




  

 

  

 