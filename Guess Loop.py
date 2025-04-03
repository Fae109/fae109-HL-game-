
def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "pls enter an integer"

    elif low is not None and high is None:
        error = ("pls enter an integer that is"
                 f"more than / = to {low}")

    else:
        error = ("pls enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:
    guess = int_check("guess:", low_num, high_num)

    if guess == "xxx":
        end_game = "yes"
        break

    #
    if guess in already_guessed:
        print(f"you've already guessed {guess}. You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"too low, pls try a higher number"
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, pls try a lower number"
                    f"you've used {guesses_used} / {guesses_allowed} guesses")
    #
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀🍀 Lucky. You got it on the first guess. 🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew. you it in {guesses_used} guesses."
        else:
            feedback = f"well done. you guessed the secret number in {guesses_used} guesses"

    #
    else:
        feedback = "sorry - you have no more guesses. you lose this round"

    print(feedback)

    #
    if guesses_used == guesses_allowed - 1:
        print("\n💣💣💣💣 Careful - you only have one guess left! 💣💣💣💣\n")

print()
print("end of round")