import random
from ending import restart_game, you_died

# Function to continually ask the Traveler for a number. Story Line C.
def guess_number():
    number = None
    while number is None:
        guess = input("Quick!, which bottle do you choose? Guess ANY number or letter: \n")
        try: 
            number = int(guess)
        except ValueError:
            print("\nThis one looks weird, try a different bottle with a number?\n")
    print(f"\nYou grab the bottle with the label, {guess} on it and drink it!")
    print("On no... you don't feel so good...")     


# Function to pick a random number. Story line A - Random container to feed
# def random_contaner():
#     number = random.randrange(1,10)
#     random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
#     while random_guess != number:
#         if random_guess < number:
#             print("That one doesn't look right, pick a higher number")
#             random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
#         else:
#             print("Doesn't look right, pick a lower number.")
#             random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
#     print("\nYou open the container and throw the food at it. Look! Its eating!")

def random_contaner():  
    while True:
        try:  
            number = random.randrange(0,11)
            random_guess = int(input("Pick a container between 1 and 10. Type your number:\n")) 
            while random_guess != number:
                if random_guess < number:
                    print("That one doesn't look right, pick a higher number")
                    random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
                elif random_guess not in range(0, 11):
                    print("Try a number between 1 and 10.)")
                    random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
                else:
                    print("Doesn't look right, pick a lower number.")
                    random_guess = int(input("Pick a container between 1 and 10. Type your number:\n"))
            print("\nYou open the container and throw the food at it. Look! Its eating!")
            break
        except ValueError:
            print("That doesn't look right, try entering a number between 1 and 10.")



# Function to guess the password for Story B - metalic box
def password_guess():
    print("You see the first letter as 'S' and the last letter as 'E'")
    count = 0
    while count < 3:
        password_guess = input("\nEnter your guess to see if it works:\n").lower().strip()
        if password_guess == "space":
            print("\nIt worked!")
            print("You saved my world!")
            print("A blinding flash of light errupts and you pass out.")
            print("Only to wake up in your backyard under a sky full of stars.")
            break
        else:
            print(f"\nYou hear 'Error, self destruct in, {3 - count}.")
            count += 1
            print("Try again")
    else:
        you_died()
        restart_game()
