"""
test_finger_exer_roots.py -- test finger_exer_roots using 
        variety of alogrithm interpretations
"""
import pytest
import sys

sys.path.append("../")

import finger_exer_roots as r

@pytest.mark.parametrize(
        "guess, power, func, exp_val",
        [
            (25, 2, r.find_root_bisection, 5),
            (-8, 3, r.find_root_bisection, -2),
            (16, 4, r.find_root_bisection, 2),
            (25, 2, r.find_root_exhaustive, 5),
            (-8, 3, r.find_root_exhaustive, -2),
            (16, 4, r.find_root_exhaustive, 2),
            (25, 2, r.find_root_newton_raphson, 5),
            (-8, 3, r.find_root_newton_raphson, -2),
            (16, 4, r.find_root_newton_raphson, 2),
        ]
)
def test_bisection_root_search(guess, power, func, exp_val):
    assert round(func(guess=guess, power=power, epsilon=.001)) == exp_val

if __name__ == '__main__':
    pytest.main()