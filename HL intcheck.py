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

# main routine

# rounds = "test"
# while rounds != "":
#     rounds = int_check("rounds <enter for infinite>:", low=1, exit_code="")
#     print(f"you asked for {rounds}")


# low_num = int_check("Low number? ")
# print(f"you chose a low number of {low_num}")

# high_num = int_check("High number? ", low=1)
# print(f"you chose a low number of {high_num}")

guess = ""
while guess != "xxx":
    guess = int_check("Guess:", low=0, high=10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()