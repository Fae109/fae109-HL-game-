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


def int_check(question):
    """checks user enters an int more than or equal to 1"""

    while True:
        error = "pls enter an integer more then or equal to 1"

        to_check = input(question)

        #
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
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
num_rounds = int_check("how many rounds would you like? push <enter> of infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

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