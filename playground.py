

correct_password = False
password = "space"
i = 0
while correct_password == False and i < 3: 
    attempted_password = input("You see the first letter as an 'S' and the last letter as a 'E'. Enter your guess to see if it works:\n").lower().strip()
    if attempted_password == password:
        print("It worked!")
        # i = 0
        correct_password = True 
    else:
        i += 1 
        print(f"\nYou hear a loud noise with a mechanical voice repeating, 'Error, Error, Error'\nTry Again! {3 - i} Attempts left.\n") 
if correct_password == True:
    print("\nYou hear a click and a whir of noises as the box opens to display a minuture galaxy.")
    # print(f"'{traveller_name}, you found it! I was looking for my home world and here it is. You SAVED my World!")
    print("A blinding flash of light errupts and you pass out. Only to wake up in your backyard under a sky full of stars.")
    print("THE END")
else:
    print("The box starts to shake in your hands and a loud noise errupts from it.\nYou DEAD.")







