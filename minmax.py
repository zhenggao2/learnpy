# -*- encoding: utf-8 -*-
def find_min_max(L):
    if len(L) == 0:
        return (None, None)
    min_val = L[0]
    max_val = L[0]
    for val in L[1:]:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    return (min_val, max_val)
    
    
