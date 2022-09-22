# Function to continually ask the Traveler for a number. Story Line C.
def guess_number():
    number = None
    while number is None:
        guess = input("Quick!, which bottle do you choose? Guess ANY number or letter: \n")
        try: 
            number = int(guess)
        except ValueError:
            print("\nThis one looks weird, try a different bottle with a number?\n")
    print(f"\nYou quickly grab the bottle with the label, {guess} on it and drink it!")
    print("On no... you don't feel so good...")     

