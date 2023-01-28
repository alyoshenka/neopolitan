"""Takes letters as defined and transforms them into usable data"""

# Todo: location?

# todo
# pylint: disable=wildcard-import
# pylint: disable=import-error
from writing.groups_8 import *
# pylint: disable=undefined-variable

from math import floor

def character_to_symbol(char):
    """Gets the symbol for the character"""
    ascii_val = ord(char)
    # todo: make everything like for symbols?
    if ascii_val >= 97 and ascii_val < 123:
        return lowercase[ascii_val-97]
    elif ascii_val >= 65 and ascii_val < 91:
        return uppercase[ascii_val-65]
    elif ascii_val >= 48 and ascii_val < 58:
        return numbers[ascii_val-48]
    elif char in symbols:
        return symbols[char]
    else:
        print("Cannot find char: " + char)
        return []

def frame_length(sym):
    """Returns the highest multiple of 8 above the largest index in the symbol array. This makes it so the frame has the correct length, since it should 'fill' all columns it uses"""
    sym_len = len(sym)
    last_idx = sym_len-1
    last_col = sym[last_idx]
    len_last_col = len(last_col)
    last_col_idx = len_last_col-1
    last_val = last_col[last_col_idx]
    # round up to next multiple of 8
    ret = -1
    if last_val % 8 == 0:
        ret = last_val
    else:
        ret = 8 * (floor(last_val / 8.0)+1)
    return ret

# Todo: dictionary: idx=color instead?
def symbol_to_array(sym, color=(255,255,255), off=None):
    """Takes a defined symbol and returns an array where the symbol is defined by indices of 'color' and 'off' values are None"""
    frame = [off for i in range(frame_length(sym))]
    for col in sym:
        for val in col:
            frame[val] = color
    return frame