"""Example test file"""

def func(x):
    """Returns x+1"""
    return x + 1


def test_answer():
    """Checks func"""
    assert func(3) == 4
