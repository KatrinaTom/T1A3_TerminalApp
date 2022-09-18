challenge_one = input("Ahead of you is a door, right next to you is a loose panel, or do you make a run for it! What do you do? Type: (door) / (panel) or (run)\n").lower().strip()
if challenge_one == "run":
    print("\nYou take off running the other direction from the noise.\nOnce you turn the corner you press yourself against the metal walls listening carefully for any noise.\n")
    challenge_two = input("But then you see a small fluffy creature with big eyes.\nDo you trust it and pick it up? Type: (Yes) / (No)\n").lower().strip()
    if challenge_two == "no":
        challenge_three = input("\nOh hell no you you say! Your mysterious friend smiles at you wisely.\n(Yes) / (No)").lower().strip()
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


