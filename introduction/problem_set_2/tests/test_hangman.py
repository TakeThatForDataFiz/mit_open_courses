import pytest
import sys
import string
sys.path.append('../')
import hangman as h


@pytest.mark.parametrize(
        "secret_word, guessed_list, exp_val",
        [
            ("apple", ['a', 'p', 'p', 'l', 'e'], True),
            ("fill", ['f', 'l', 'g'], False),
        ]
)
def test_is_word_guessed(secret_word, guessed_list, exp_val):
    assert h.is_word_guessed(secret_word=secret_word, letters_guessed=guessed_list) == exp_val


@pytest.mark.parametrize(
        "secret_word, guessed_list, exp_val",
        [
            ("apple", ['a', 'e'], "a _ _ _ e"),
            ("fill", ['b'], "_ _ _ _"),
        ]
)
def test_guessed_word(secret_word, guessed_list, exp_val):
    assert h.get_guessed_word(secret_word=secret_word, letters_guessed=guessed_list) == exp_val

@pytest.mark.parametrize(
        "letters, exp_val",
        [
            (['a', 'b', 'c', 'd', 'e', 'f'], 'ghijklmnopqrstuvwxyz'),
            (['e', 'i', 'k', 'p', 'r', 's'], 'abcdfghjlmnoqtuvwxyz')
        ]
)
def test_get_avail_letters(letters, exp_val):
    assert h.get_available_letters(letters_guessed=letters) == exp_val

@pytest.mark.parametrize(
        "my_word, other_word, exp_val",
        [
            ("t e _ t", "tact", False),
            ("a _ _ _ e", "banana", False),
            ("a _ _ _ e", "apple", True),
            ("a _ p p l e", "apple", False),
        ]
)
def test_match_with_gaps(my_word, other_word, exp_val):
    assert h.match_with_gaps(my_word=my_word, other_word=other_word) == exp_val


@pytest.mark.parametrize(
        "my_word, exp_val",
        [
            ("abbbbb_", "No Matches Found"),
            ("t_ _ t", ['tact', 'tart', 'taut', 'teat', 'tent',
                        'test', 'text', 'that', 'tilt', 'tint',
                        'toot', 'tort', 'tout', 'trot', 'tuft',
                        'twit']),
            ("a_ pl_ ", ['ample', 'amply']),
        ]
)
def test_show_possible_matches(my_word, exp_val):
    assert h.show_possible_matches(my_word=my_word) == exp_val

if __name__ == '__main__':
    pytest.main()