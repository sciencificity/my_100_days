import pytest
from day26_27_fizzbuzz import fizzbuzz
# def test_fizzbuzz_initial():
#     assert fizzbuzz(1) == 1
#     assert fizzbuzz(2) == 2
#     assert fizzbuzz(3) == 'Fizz'
#     assert fizzbuzz(5) == 'Buzz'
    # we can see this is getting very repetitive

# pytest has this nice parametrize feature where we can give it a list of tuples
# of argument and expected return values in a decorator
# In the function we can just call the func with arg and test it against return
@pytest.mark.parametrize("arg, ret",[
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
    (16, 16),
])
def test_fizzbuzz(arg, ret):
    assert fizzbuzz(arg) == ret

