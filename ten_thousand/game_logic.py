from collections import Counter
import random


class GameLogic:
    @staticmethod
    def roll_dice(n):
        """
        Rolls n 6-sided dice.
        :param n: Number of dice.
        :return: Tuple of dice rolls.
        """
        rolls = tuple(random.randint(1, 6) for _ in range(n))
        return rolls

    @staticmethod
    def is_cheating(roll, keepers):
        """
        Returns True if a user is trying to cheat (or misclicks).
        :param roll: Tuple of integers, representing the dice roll.
        :param keepers: String of kept dice from the user.
        :return: True if cheating, False if not.
        """
        # https://docs.python.org/3/library/collections.html#counter-objects
        # https://replit.com/@AdamOwada/AngryAnimatedBlogclient#main.py
        return 

    @staticmethod
    def calculate_score(roll):
        """
        Scores a give roll according to the rules of Ten Thousand.
        :param roll: A tuple of integers representing dice values.
        :return: An integer representing the score.
        """
        roll = Counter(roll)
        score = 0

        # Check for straight
        if len(roll) == 6:
            return 1500

        # Check for 3 pair
        if len(roll) == 3 and roll.most_common()[0][1] == 2:
            return 1500

        # 3 or more of any number
        for i in range(1, 7):
            quantity = roll[i]
            if quantity >= 3:
                if i == 1:
                    score += (quantity - 2) * 1000
                else:
                    score += (quantity - 2) * i * 100

        # 1s and 5s
        score += 100 if roll[1] == 1 else 0
        score += 200 if roll[1] == 2 else 0
        score += 50 if roll[5] == 1 else 0
        score += 100 if roll[5] == 2 else 0

        return score
