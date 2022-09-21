# You died function AND Restart

def you_died():
    print("You Died!")
    print("That is the end of your Space Adventure.")


def finished_story():
    print("THE END")
    print("That is the end of your Space Adventure.")


def restart_game():
    restart = input("Would you like to play again? Type: (Yes) / (No)\n").lower()
    if restart == 'yes' or restart == 'y':
        return
    else:
        print("Maybe next time.")
        exit()




