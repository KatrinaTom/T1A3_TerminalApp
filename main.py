# Choose Your Own Adventure Application 

# Instructions 
print('*********************************************************************************************')
print('Welcome!')
print('The instructions are simple.')
print('A mysterious creature has transported you to a remote outpost station in Space.')
print('You don\'t recognise the stars or planets, but outside you see a rainbow of colours that take your breath away, you must be in a stellar nursery.\n')
print('Along the way the mysterious creature will ask you questions, also you may encounter some challenges and puzzles to test your skills and knowledge!\n')
print('To wake up from this strange dream, if it even is a dream, type in quit() at any time.\n')

# Are you ready to begin Control Flow
start_adventure = input("Are you ready for your journey? (Yes/No) \n").capitalize()

while True:
    if start_adventure == "Yes":
        print('Lets begin!\n')
    

# Main Story 

        print('Welcome Space Traveller')
        print('I have brought you here as we are in grave danger and I need your help!')
        print('You look around and realise you have been transported to the distant future where everything looks strange and computerised.')
        print('The mysterious creature is looking at you and asks.')
        traveller_name = input('What shall I call you?\n')
        print(f'Ah excellent, it is a bit hard for me to say this, but I will call you {traveller_name}!\n')
        print(f'The mysterious creature points ahead of you and says, {traveller_name} we need to go that way')

        challenge_one = input("Ahead of you is a door, right next to you is a loose panel, or do you make a run for it! What do you do? Type: (door) / (panel) or (run)\n").lower().strip()
        if challenge_one == "run":
            print("\nYou take off running the other direction from the noise.\nOnce you turn the corner you press yourself against the metal walls listening carefully for any noise.\n")
            challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you trust it and pick it up? Type: (Yes) / (No)\n").lower().strip()
            if challenge_two == "no":
                print(f"\nOh hell no you say! Your mysterious friend smiles at you wisely and says '{traveller_name}, a wise decision, they can bite your hand off!'.\n")
                challenge_three = input(f"{traveller_name}, we really must go, there is ...")
                if challenge_three == "Yes":
                    print("Yes!")
                elif challenge_three == "No":
                    print("Oh no :( ")
                else:
                    print("What just happened?")
            else:
                print("\nAww how cute you think to youself.\nAs you reach out with your hand you see this giant mouth open wide with razor sharp teeth!\nIn an instance your arm is bitten off and you pass out from blood loss.\nYou DEAD!")
        elif challenge_one == "panel":
            print("\nYou sqeeze into the tight space, quickly covering the panel back into place. Holding your breath waiting and listening!\nNext minute you hear slithering sounds near your panel.\nThen a loud thump on the panel!\nThe panel opens to reveal...\nYou passed out!") 
        else:
            print("\nYou try to push the door. Oh no! Its stuck. But you gave it a hard push and it swooshes open.\nOnly to reveal a room full of poisionous plants!\nYou accidentally brushed against one in your haste and start to feel sick. What are these purple lumps on you?\nOn no... as you swell up and POP!\nYou DEAD!")

    
    else: 
        print('Maybe next time.!')
        break


  

 