"""Test groups"""


# ToDo: fix this
# pylint: disable=import-error
# pylint: disable=wildcard-import
# pylint: disable=undefined-variable
from src.writing.letters_8 import *
from src.writing.groups_8 import *



def test_all_letters_used():
    """Tests that all defined symbols are put into a group"""
    len_groups = len(uppercase) + len(lowercase) + len(symbols) + len(numbers)
    len_letters = DEFINED_UPPERCASE + DEFINED_LOWERCASE + DEFINED_SYMBOLS + DEFINED_NUMBERS
    assert len_groups == len_letters, 'The number of symbols defined should be the same either way'