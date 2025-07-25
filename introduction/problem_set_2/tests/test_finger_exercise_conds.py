import pytest
import sys
sys.path.append('../')
from finger_exercise_conds import get_special_odd

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

if __name__ == "__main__":
    pytest.main()