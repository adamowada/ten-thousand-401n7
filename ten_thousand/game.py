try:
    from ten_thousand.game_logic import GameLogic
except:
    from game_logic import GameLogic


def play(roller=GameLogic.roll_dice):  # new param
    """
    Entry point into Ten Thousand game.
    :param roller: Default is the normal random roller static method. Optionally pass in reference to GameLogic
    instance's .mock_roller method.
    :return:
    """
    welcome = input("Welcome to Ten Thousand\n(y)es to play or (n)o to decline\n> ")
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
        print(f"You banked {result} points in round {round_number}\nTotal score is {total_score} points")
    print(f"Thanks for playing. You earned {total_score} points")


def do_round(round_number, roller):
    print(f"Starting round {round_number}")
    dice_remaining = 6
    unbanked_points = 0
    while dice_remaining:
        roll = roller(dice_remaining)
        print(f"Rolling {dice_remaining} dice...")
        print_dice(roll)
        # do zilch! # 2nd new
        if GameLogic.calculate_score(roll) == 0:   # new
            do_zilch()  # new
            return 0  # new
        keepers = do_keepers(roll)  # 3rd new add roll argument
        if keepers == "q":
            return "q"
        unbanked_points += GameLogic.calculate_score(keepers)
        dice_remaining -= len(keepers)
        # do hot dice! 1st
        if dice_remaining == 0:  # new
            dice_remaining = 6  # new (or could do in function)
        rbq = do_rbq(unbanked_points, dice_remaining)
        if rbq == "b":
            return unbanked_points
        if rbq == "q":
            return "q"


def do_rbq(unbanked_points, dice_remaining):
    rbq = input(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:\n> ")
    return rbq


def print_dice(dice):
    print(f"*** {' '.join([str(i) for i in dice])} ***")


def do_keepers(roll):  # add roll parameter
    """Asks user if they want to keep dice, or quit. Returns choice"""
    while True:  # new
        keepers = input("Enter dice to keep, or (q)uit:\n> ")
        if keepers == "q":
            return "q"
        keepers = tuple(int(num) for num in keepers if num.isnumeric())
        # verify the keepers! are the cheating?
        cheating = GameLogic.is_cheating(roll, keepers)  # new
        if not cheating:  # new
            break  # new
        print("Cheater!!! Or possibly made a typo...")  # new
        print_dice(roll)  # new
    return keepers  # function-level scoping


def do_hot_dice():
    pass


def do_zilch():  # new
    print("****************************************")  # new
    print("**        Zilch!!! Round over         **")  # new
    print("****************************************")  # new


if __name__ == "__main__":
    test = GameLogic([(1,2,3,4,5,6)])
    play(test.mock_roller)
