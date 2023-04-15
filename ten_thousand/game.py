<<<<<<< HEAD
try:
    from ten_thousand.game_logic import GameLogic
except ModuleNotFoundError:
    from game_logic import GameLogic


def play(roller=GameLogic.roll_dice):  # new param
    """
    Entry point into Ten Thousand game.
    :param roller: Default is the normal random roller static method. Optionally pass in reference to GameLogic
    instance's .mock_roller method.
    :return:
    """
=======
from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice):
>>>>>>> main
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    welcome = input("> ")
    if welcome == "n":
        print("OK. Maybe another time")
        return

    total_score = 0

    # Do 20 rounds
    for round_number in range(1, 21):
        result = do_round(round_number, roller)
        if result == "q":
            break  # exits for loop
        total_score += result
        print(f"You banked {result} points in round {round_number}")
        print(f"Total score is {total_score} points")
    print(f"Thanks for playing. You earned {total_score} points")


def do_round(round_number, roller):
    print(f"Starting round {round_number}")
    dice_remaining = 6
    unbanked_points = 0
    while dice_remaining:
        roll = roller(dice_remaining)
        print(f"Rolling {dice_remaining} dice...")
        print_dice(roll)
<<<<<<< HEAD
        # do zilch! # 2nd new
        if GameLogic.calculate_score(roll) == 0:   # new
            do_zilch()  # new
            return 0  # new
        keepers = do_keepers(roll)  # 3rd new add roll argument
=======
        # do zilch!
        if GameLogic.calculate_score(roll) == 0:
            do_zilch()
            return 0
        keepers = do_keepers(roll)  # new argument/param
>>>>>>> main
        if keepers == "q":
            return "q"
        unbanked_points += GameLogic.calculate_score(keepers)
        dice_remaining -= len(keepers)
<<<<<<< HEAD
        # do hot dice! 1st
        if dice_remaining == 0:  # new
            dice_remaining = 6  # new (or could do in function)
=======
        # do hot dice!
        if dice_remaining == 0:
            dice_remaining = 6
>>>>>>> main
        rbq = do_rbq(unbanked_points, dice_remaining)
        if rbq == "b":
            return unbanked_points
        if rbq == "q":
            return "q"


def do_rbq(unbanked_points, dice_remaining):
    print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    rbq = input("> ")
    return rbq


def print_dice(dice):
    # print("***", *dice, "***")
    print(f"*** {' '.join([str(i) for i in dice])} ***")


<<<<<<< HEAD
def do_keepers(roll):  # add roll parameter
    """Asks user if they want to keep dice, or quit. Returns choice"""
    while True:  # new
=======
def do_keepers(roll):
    """Asks user if they want to keep dice, or quit, validates input. Returns choice"""
    while True:
>>>>>>> main
        print("Enter dice to keep, or (q)uit:")
        keepers = input("> ")
        if keepers == "q":
            return "q"
<<<<<<< HEAD
        keepers = tuple(int(num) for num in keepers if num.isnumeric())
        # verify the keepers! are the cheating?
        cheating = GameLogic.is_cheating(roll, keepers)  # new
        if not cheating:  # new
            break  # new
        print("Cheater!!! Or possibly made a typo...")  # new
        print_dice(roll)  # new
    return keepers  # function-level scoping
=======

        # turn the keepers string into a tuple of ints
        keepers = tuple(int(num) for num in keepers if num.isnumeric())

        # verify the keepers! are the cheating?
        cheating = GameLogic.is_cheating(roll, keepers)
        if not cheating:
            # let them leave the while loop
            break

        print("Cheater!!! Or possibly made a typo...")
        print_dice(roll)
    return keepers
>>>>>>> main


def do_zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def do_zilch():  # new
    print("****************************************")  # new
    print("**        Zilch!!! Round over         **")  # new
    print("****************************************")  # new


if __name__ == "__main__":
<<<<<<< HEAD
    test = GameLogic([(1,2,3,4,5,6)])
    play(test.mock_roller)
=======
    test_straight = GameLogic([(1, 2, 3, 4, 5, 4)])
    # play(test_straight.mock_roller)
    play()
>>>>>>> main
