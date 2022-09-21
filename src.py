# Function to continually ask the Traveler for a number. Story Line C. 

def number_guess(prompt):
    result = None
    while result is None:
        user_input = input(prompt)
        try: 
             result = int(user_input)
        except ValueError:
            print("This one looks weird, try a different bottle with a number?\n\n")
    return result

