import pytest
import sys
sys.path.append('../')
from finger_exercise_conds import get_special_odd, is_even

def get_special_odd_wrapper(num):
    get_special_odd(num_1=num, num_2=num, num_3=num)

@pytest.mark.parametrize(
        "num_1, num_2, num_3, exp_value",
        [
            (1, 3, 5, 5),
            (2, 4, 6, 2),
            (5, 6, 7, 7),
            (2, 5, 4, 5),
        ]
)
def test_get_special_odd(num_1, num_2, num_3, exp_value):
    get_special_odd(num_1=num_1, num_2=num_2, num_3=num_3) == exp_value

@pytest.mark.parametrize(
        "num, exp",
        [
            (1, False),
            (2, True),
            (0, True),
        ]
)
def test_is_even(num, exp):
    assert is_even(num) == exp

@pytest.mark.parametrize(
        "num, func, excp",
        [
            ("bad", is_even, TypeError),
            ("bad", get_special_odd_wrapper, TypeError),
        ]
)
def test_excp_raises(num, func, excp):
    with pytest.raises(excp):
        func(num)

if __name__ == "__main__":
    pytest.main()