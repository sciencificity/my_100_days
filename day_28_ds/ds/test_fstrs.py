from fstrs import allowed_driving, fib
import pytest

@pytest.mark.parametrize("arg1, arg2, ret",[
    ('bob', 23, True),
    ('mark', 16, False),
    ('border', 18, True),
    ('anna', 19, True),
    ('simba', 8, False),
])
def test_allowed_driving(arg1, arg2, ret):
    assert allowed_driving(arg1, arg2) == ret
    
    
# capfd is a feature of pytest - which captures the standard output of the program and execution
# The reason we use this is that for the allowed_driving we want to check the boolean return 
# and the actual output ... {name} is allowed / not allowed drive.
@pytest.mark.parametrize("arg1, arg2, ret",[
    ('bob', 23, True),
    ('border', 18, True),
    ('anna', 19, True),
])
def test_allowed_drive_true(arg1, arg2, ret, capfd):
    assert allowed_driving(arg1, arg2) == ret
    # To see what is being printed to the console we use the capfd 
    # We re-direct the standard output, and throw away the error
    # Call the readouterr() func of capfd
    out = capfd.readouterr()[0]
    # We can just see what that gives us by using print statements
    # When calling pytest use pytest -s filename.py
    # print(out)
    # Now we can assert on that just as we do any other variables and functions
    # We use the rstrip() to strip of the new line at the right (we saw this in the print)
    assert out.rstrip() == f'{arg1} is allowed to drive'

    
@pytest.mark.parametrize("arg1, arg2, ret",[
    ('mark', 16, False),
    ('simba', 8, False),
])
def test_allowed_drive_false(arg1, arg2, ret, capfd):
    assert allowed_driving(arg1, arg2) == ret
    # To see what is being printed to the console we use the capfd 
    # We re-direct the standard output, and throw away the error
    # Call the readouterr() func of capfd
    out = capfd.readouterr()[0]
    # We can just see what that gives us by using print statements
    # When calling pytest use pytest -s filename.py
    # print(out)
    # Now we can assert on that just as we do any other variables and functions
    # We use the rstrip() to strip of the new line at the right (we saw this in the print)
    assert out.rstrip() == f'{arg1} is not allowed to drive'    

# Test that neg args to fib raise an error
def test_neg_fib():
    with pytest.raises(ValueError):
        fib(-1)

# Test that zero and one return 0, 1 as the first 2 fib numbers are 0, 1        
def test_zero_one_fib():
    assert fib(0) == 0
    assert fib(1) == 1        

# Test fib with legit values against expected output
# fib 0, 1, 1, 2, 3, 5, 8, 13, 21
@pytest.mark.parametrize("arg1, ret",[
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8),
    (7,13),
])
def test_fib(arg1, ret):
    assert fib(arg1) == ret
