"""
finger_exer_loop.py -- print largest odd number entered, print message if no odd was entered
"""
from finger_exercise_conds import is_even
import copy

def get_number():
    try:
        return int(input("Please enter a valid number: "))
    except ValueError:
        print("Invalid number entered please try again")
        return get_number()

def get_num_list(entries):
    count = 0
    nums = []
    while count < entries:
        nums.append(get_number())
        count += 1
    return nums

def get_largest_odd(nums):
    count = 0
    odds = []
    while count <= len(nums)-1:
        if not is_even(nums[count]):
            odds.append(nums[count])
        count += 1
    if not odds:
        return 0
    else:
        return max(odds)


if __name__ == "__main__":
    ENTRIES = 10
    input = get_num_list(entries=ENTRIES)
    output = get_largest_odd(nums=input)
    if output == 0:
        print("No odd numbers entered")
    else:
        print(f"Largest odd number entered is - {output}")
    