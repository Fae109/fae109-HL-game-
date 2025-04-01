import math
def yes_no(question):
    """checks user response a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # make sure user says yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(" pls enter yes or no")


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***


    """)


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_quesses = max_upped + 1
    return max_quesses

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

# main

# initialise game
mode = "regular"
rounds_played = 0

print()
print("⬆️⬆️⬆️⬆️ welcome to 5ye High Lower Game ⬇️⬇️⬇️⬇️")
print()

want_instructions = yes_no("do you want to see the instructions?")

# ask viewer if they want (cheek they say yes / no)
if want_instructions == "yes":
    instructions()


# ask user for No. of round or infinite mode
num_rounds = int_check("how many rounds would you like? push <enter of infinite mode>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#
low_num = int_check("low number?")
high_num = int_check("High Number?", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)

# game loop starts here
while rounds_played < num_rounds:

    # round heading
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ️♾️♾️♾️♾️"
    else:
        round_heading = f"\n 💿💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿💿"

    print(round_heading)
    print()

    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if
    if mode == "infinite":
        num_rounds += 1


# game loop ends

# game history / stats area