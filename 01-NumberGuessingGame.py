import random

def guessing_game():
    number = random.randint(0, 100)
    tries = 3
    
    while tries > 0:
        guessed_number = input("Please guess the number")
        
        if guessed_number.isdigit():
            guessed_number = int(guessed_number)
            if guessed_number == number:
                print('Just right')
                break
            elif guessed_number > number:
                print("Too high")
                tries -= 1
                print(f"Remaining hearts: {tries}")
            else:
                print("Too low")
                tries -= 1
                print(f"Remaining hearts: {tries}")
        else:
            print("This is not a number bro!")
    if tries == 0:
        print(f"Out of tries! The number was {number}.")
        

guessing_game()
