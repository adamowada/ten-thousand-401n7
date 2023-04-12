from game_logic import GameLogic


def play():
    welcome = input("Welcome to Ten Thousand\n(y)es to play or (n)o to decline\n> ")
    if welcome == "n":
        print("OK. Maybe another time")
        return

    banked_points = 0

    # Do 20 rounds
    for i in range(1, 21):
        result = do_round(i)
        if result == "q":
            break
        banked_points += result
        print(f"You banked {result} points in round {i}\nTotal score is {banked_points} points")
    print(f"Thanks for playing. You earned {banked_points} points")


def do_round(round_number):
    print(f"Starting round {round_number}")
    dice_remaining = 6
    unbanked_points = 0
    while dice_remaining:
        print(f"Rolling {dice_remaining} dice...")
        roll = GameLogic.roll_dice(dice_remaining)
        print_dice(roll)
        keepers = do_keepers()
        if keepers == "q":
            return "q"
        unbanked_points += GameLogic.calculate_score(keepers)
        dice_remaining -= len(keepers)
        rbq = do_rbq(unbanked_points, dice_remaining)
        if rbq == "q":
            return "q"
        if rbq == "b":
            return unbanked_points


def print_dice(dice):
    print(f"*** {' '.join([str(i) for i in dice])} ***")


def do_keepers():
    keepers = input("Enter dice to keep, or (q)uit:\n> ")
    if keepers == "q":
        return "q"
    return tuple([int(i) for i in keepers])


def do_rbq(unbanked_points, dice_remaining):
    rbq = input(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:\n> ")
    return rbq


if __name__ == "__main__":
    play()

