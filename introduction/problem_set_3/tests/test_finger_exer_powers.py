"""
test_finger_exer_powers.py
    -- test powers exercise script
"""
import pytest
import sys

sys.path.append("../")
import finger_exer_powers as p

@pytest.mark.parametrize(
    "input, exp_val",
    [
    (25, [5, 2]),
    (8, [2, 3]),
    (11, None),
]
)
def test_finger_power_exer(input, exp_val):
    assert p.get_root_and_power(input) == exp_val 

if __name__ == "__main__":
    pytest.main()
