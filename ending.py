
# Ending functions


def you_died():
    print("\nYou Died!")
    print("That is the end of your Space Adventure.")


def finished_story():
    print("\nTHE END")
    print("That is the end of your Space Adventure.")


def restart_game():
    restart = input("\nWould you like to play again? Type: (Yes) / (No)\n").lower()
    if restart == 'yes' or restart == 'y':
        print("Lets Begin!")

    elif restart == 'no' or restart == 'n':
        print("Sorry to see you go.")
        exit()

    else:
        print("Maybe next time.")
        exit()




