challenge_one = input("Ahead of you is a door, and you see a loose panl, or you make a run for it! What do you do? Type: (door) / (panel) or (run)\n").lower().strip()
if challenge_one == "run":
    print("You take off running the other direction from the noise.\nOnce you turn the corner you press yourself against the metal walls listening carefully for any noise.\n")
    challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you trust it and pick it up? Type: (Yes) / (No)\n").lower().strip()
    if challenge_two == "no":
        challenge_three = input("Oh hell no you you say! Your mysterious friend smiles at you wisely.\n")
        if challenge_three == "Yes":
            print("")
        elif challenge_three == "No":
                print("")
        else:
            print("")
    else:
        print("Aww how cute you think to youself.\nAs you reach out with your hand you see this giant mouth open wide with razor sharp teeth!\nIn an instance your arm is bitten off and you pass out from bloos loss.\nYou DEAD!")
elif challenge_one == "panel":
    print("You sqeeze into the tight space, quickly covering the panel back into place. Holding your breath waiting and listening!") 
else:
    print("You try to push the door. Oh no! Its stuck. But you gave it a hard push and it swooshes open.\nOnly to reveal a room full of poisionous plants!\nYou accidentally brushed against one in your haste and start to feel sick. What are these purple lumps on you?\nOn no... as you swell up and POP! \n You DEAD!")


