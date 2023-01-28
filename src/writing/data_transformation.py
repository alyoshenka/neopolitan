"""Takes letters as defined and transforms them into usable data"""

# Todo: location?

def frame_length(sym):
    """Returns the highest multiple of 8 (- 1) above the largest index in the symbol array. This makes it so the frame has the correct length, since it should 'fill' all columns it uses"""
    sym_len = len(sym)
    last_idx = sym_len-1
    last_col = sym[last_idx]
    len_last_col = len(last_col)
    last_col_idx = len_last_col-1
    last_val = last_col[last_col_idx]
    # round up to next multiple of 8
    return 8 * round(last_val / 8.0)

# Todo: dictionary: idx=color instead?
def symbol_to_array(sym, color=(255,255,255), off=None):
    """Takes a defined symbol and returns an array where the symbol is defined by indices of 'color' and 'off' values are None"""
    frame = [off for i in range(frame_length(sym))]
    for col in sym:
        for val in col:
            frame[val] = color
    return frame