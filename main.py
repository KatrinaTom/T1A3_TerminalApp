# Choose Your Own Adventure Application 

# Instructions 
print('*********************************************************************************************')
print('Welcome!')
print('The instructions are simple.')
print('A mysterious creature has transported you to a remote outpost station in Space.')
print('You don\'t recognise the stars or planets, but outside you see a rainbow of colours that take your breath away, you must be in a stellar nursery.\n')
print('Along the way the mysterious creature will ask you question, also you may encounter some challenges and puzzles to test your skills and knowledge!\n')
print('To wake up from this strange dream, if it even is a dream, type in quit() at any time.\n')

# Are you ready to begin Control Flow
start_adventure = input("Are you ready for your journey? (Yes/No) \n").capitalize()

while True:
    if start_adventure == "Yes":
        print('Lets begin!\n')
    else: 
        print('Maybe next time.!')
        break

# Main Story 

    print('Welcome Space Traveller')
    print('I have brought you here as we are in grave danger and I need your help!')
    print('You look around and realise you have been transported to the distant future where everything looks strange and computerised.')
    print('The mysterious creature is looking at you and asks.')
    traveller_name = input("What shall I call you?\n")
    print(f'Ah excellent, it is a bit hard for me to say this, but I will call you {traveller_name}!').capitalize().strip()


# First Challenge 

    



  

 