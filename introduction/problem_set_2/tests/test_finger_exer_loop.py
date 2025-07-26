import pytest 
import sys 

sys.path.append("../")
import finger_exer_loop as fe


def test_get_number(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 4)
    assert fe.get_number() == 4

@pytest.mark.parametrize(
        "num, entries, exp_val",
        [
            (1, 5, [1, 1, 1, 1, 1]),
            (4, 2, [4, 4]),
            (5, 10, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),
        ]
)
def test_get_number_list(monkeypatch, num, entries, exp_val):
    monkeypatch.setattr('finger_exer_loop.get_number', lambda: num)
    assert fe.get_num_list(entries=entries) == exp_val

@pytest.mark.parametrize(
        "input, exp_val",
        [
            ([5, 3], 5),
            ([2, 4], 0),
            ([1, 2, 7], 7),
        ]
)
def test_get_largest_odd(input, exp_val):
    assert fe.get_largest_odd(nums=input) == exp_val

if __name__ == "__main__":
    pytest.main()