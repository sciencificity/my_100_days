from day26_27_guess import get_random_number, Game
from unittest.mock import patch
import random
import pytest

# We are going to mock an object since our function get_random_number 
# uses a random integer but random returns something randomly 
# So how do we test if the random is giving us a diff integer each time?
# The idea is to mock an object!
# use @patch.object -> it is the random module -> and it is the randint method we want to patch
@patch.object(random, 'randint')
# Now in the test method we pass in an argument and we give that argument a fixed return value
# This is key - instead of having random return something new each time, we can give it a fixed value
# So it's an override of what randint does -> it says everytime randint is called return 17
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17

# Here we simulate the input() call to get the user input.
# The side_effects can be a list of values, and we will try and run through to get all the different errors
# as though the user entered those values
@patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5,
                                      -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError):
        game.guess()
    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # user hit enter - we can't test assert game.guess() == None - it does not work, throws a ValueError so
    # use this code instead
    with pytest.raises(ValueError):
        game.guess()

# capfd is a feature of pytest - which captures the standard output of the program and execution
# The reason we use this is that for the validate_guess_method we want to check the boolean return 
# and the actual output ... {guess} is too high, too low etc. because this is a game
# and we want to test that the output we give the user is accurate too
def test_validate_guess(capfd):
    game = Game()
    # Set answer of game to 2
    game._answer = 2

    # Check that 1 is not the answer of the Game using `assert not` this time
    assert not game._validate_guess(1)
    # To see what is being printed to the console we use the capfd 
    # We re-direct the standard output, and throw away the error
    # Call the readouterr() func of capfd
    out, _ = capfd.readouterr()
    # We can just see what that gives us by using print statements
    # When calling pytest use pytest -s filename.py
    # print(out)
    # Now we can assert on that just as we do any other variables and functions
    # We use the rstrip() to strip of the new line at the right (we saw this in the print)
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'

## Run a game end to end - win scenario
# We again use the mock by simulating a user inputting values
@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(inp, capfd):
    game = Game()
    game._answer = 6

    game()
    assert game._win is True

    # Here we use 0 indexing so that we can do away with the out, _
    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range',
                '9 is too high', 'Already guessed',
                '6 is correct!', 'It took you 3 guesses']

    output = [line.strip() for line
              in out.split('\n') if line.strip()]
    # Look over expected and output lists in parallel and see if they match
    for line, exp in zip(output, expected):
        assert line == exp

## Run a game end to end - lose scenario
@patch("builtins.input", side_effect=[None, 5, 9, 14, 11, 12])
def test_game_lose(inp, capfd):
    game = Game()
    game._answer = 13

    game()
    assert game._win is False
