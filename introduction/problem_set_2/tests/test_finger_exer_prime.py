import pytest 
import sys 

sys.path.append("../")
import finger_exer_prime as fe

# TODO: INSERT TEST CASES
@pytest.mark.parametrize(
        "input, exp",
        [
            (3, True),
            (7, True),
            (9, False),
            (8, False),
            (0, False),
            (1, False)
        ]
)
def test_prime_cases(input, exp):
    assert fe.is_prime(num=input) == exp


@pytest.mark.parametrize(
        "exp",
        [
            (76125),
        ]
)
def test_get_sum_primes(exp):
    assert fe.get_sum_primes() == exp


if __name__ == "__main__":
    pytest.main()