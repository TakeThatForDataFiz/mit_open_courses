import pytest
import ps1a as ps1

@pytest.mark.parametrize(
        "filename, exp_val",
        [
            ("test_ps1_cow_data.txt", {"Maggie": 3, "Herman": 7, "Betsy": 9}),
        ]
)
def test_load_cows(filename, exp_val):
    assert ps1.load_cows(filename) == exp_val

@pytest.mark.parametrize(
        "cows, limit, exp_val",
        [
            ({"Maggie": 3, "Herman": 7, "Betsy": 9}, 10, [["Betsy"], ["Herman", "Maggie"]]),
            ({"Ben": 5, "John": 5}, 10, [["Ben", "John"]]),
            ({"Chris": 9, "Clemson": 8, "Harley": 10}, 10, [["Harley"], ["Chris"], ["Clemson"]])
        ]
)
def test_greedy_cow_transport(cows, limit, exp_val):
    assert ps1.greedy_cow_transport(cows=cows, limit=limit) == exp_val

@pytest.mark.parametrize(
        "cows, limit, exp_val",
        [
            ({"James": 5, "Paul": 3, "Peter": 2}, 10, [["James", "Peter", "Paul"]]),
            ({"Maggie": 3, "Herman": 7, "Betsy": 9}, 10, [["Betsy"], ["Herman", "Maggie"]]),
            ({"Chris": 9, "Clemson": 8, "Harley": 10}, 10, [["Harley"], ["Chris"], ["Clemson"]])
        ]
)
def test_brute_force_cow_transport(cows, limit, exp_val):
    assert ps1.brute_force_cow_transport(cows=cows, limit=limit).sort() == exp_val.sort()

if __name__ == "__main__":
    pytest.main()