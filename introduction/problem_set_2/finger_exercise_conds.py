"""
finger_exercise_conds.py -- script returning largest of 3 numbers if odd,
                                otherwise return smallest number
"""

def get_special_odd(num_1: int, num_2: int, num_3: int):
    if num_1 % 2 == 0 and num_2 % 2 == 0 and num_3 % 2 == 0:
        return min(num_1, num_2, num_3)
    else:
        odds = []
        if num_1 % 2 != 0:
            odds.append(num_1)
        if num_2 % 2 != 0:
            odds.append(num_2)
        if num_3 % 2 != 0:
            odds.append(num_3)
        if not odds:
            raise ValueError(f"Values - 1){num_1} 2){num_2} 3){num_3} passed are invalid")
        return max(odds)