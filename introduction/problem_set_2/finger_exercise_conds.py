"""
finger_exercise_conds.py -- script returning largest of 3 numbers if odd,
                                otherwise return smallest number
"""

def is_even(num):
    return num % 2 == 0

def get_special_odd(num_1: int, num_2: int, num_3: int):
        odds = []
        if not is_even(num_1):
            odds.append(num_1)
        if not is_even(num_2):
            odds.append(num_2)
        if not is_even(num_3):
            odds.append(num_3)
        if not odds:
            return min(num_1, num_2, num_3)
        else:
            return max(odds)
        