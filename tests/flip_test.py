"""Tests whether the 'flip' functionality is implemented correctly"""

from hardware.board_display import BoardDisplay

"""
0 0 0 -> 0 1 0
1 1 1    1 0 1
"""

def test_flip():
    initial_data = [0,1,0,1,0,1]
    expected_data = [0,1,1,0,0,1]
    height = 2
    
    assert BoardDisplay.flip(initial_data, height=height) == expected_data, 'Flipped data does not match expected'