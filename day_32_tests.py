from day_32_code import print_game_stats, games_won
from day_32_code import split_in_columns


def test_print_game_stats(capfd):
    winner_prints = ["sara has won 0 games",
                     "bob has won 1 game",
                     "tim has won 5 games",
                     "julian has won 3 games",
                     "jim has won 1 game"]

    print_game_stats(games_won)
    output = capfd.readouterr()[0].splitlines()

    # dict + Python 3.7 = insert order should be retained
    for line in winner_prints:
        assert line in output


def test_split_in_columns_default_message():
    # one line string but a nice way in Python to wrap over multiple lines
    expected = ('Hello world!|We hope that you are learning a lot of Python.|'
                'Have fun with our Bites of Py.|Keep calm and code in Python!'
                '|Become a PyBites ninja!')

    actual = split_in_columns()
    assert actual == expected


def test_split_in_columns_on_other_message():
    expected = 'Hello world:|I am coding in Python :)|How awesome!'

    message = 'Hello world:\nI am coding in Python :)\nHow awesome!'
    actual = split_in_columns(message)

    assert actual == expected
