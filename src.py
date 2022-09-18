# Function to continually ask the Traveler for a number. 

def number_guess(prompt):
    
    result = None
    
    while result is None:
        
        user_input = input(prompt)

        try: 
             result = int(user_input)
        except ValueError:
            print("That wasn't the right one, try maybe the bottle with a number?\n\n")
        
    return result
