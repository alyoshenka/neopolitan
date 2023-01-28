
# ToDo: fix this
# pylint: disable=import-error
# pylint: disable=wildcard-import
# pylint: disable=undefined-variable
from src.writing.letters_8 import *
from src.writing.data_transformation import frame_length
from src.writing.data_transformation import symbol_to_array

def test_frame_length():
    """Ensure that frame_length returns the correct length for given arrays"""

    # Todo: more tests necessary?
    assert frame_length(a) == 32, '"a" should take up 32 indices'
    assert frame_length(i) == 8, '"i" should take up 8 indices'
    assert frame_length(DOLLAR) == 40, '"$" should take up 40 indices'

def test_symbol_to_array():
    """Test that symbol_to_array correctly calculates array form"""

    # Use '1' instead of color for easier reading
    a_array = [0,0,0,0,0,1,0,0, 0,0,1,0,1,0,1,0, 0,0,1,0,1,0,1,0, 0,0,0,1,1,1,1,0]
    assert symbol_to_array(a, color=1, off=0) == a_array, 'Data array does not match expected'

    