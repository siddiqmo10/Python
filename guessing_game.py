secret_number = 9
guesses = 0

while guesses < 3:
    user_input = int(input("Guess: "))
    guesses += 1
    if user_input == secret_number:
        print("You guessed it right")
        break

# this else is for while when we break out of it
else:
    print("Sorry! You are out of guesses")