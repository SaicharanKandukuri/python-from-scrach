def least_difference(a, b, c):
    """ 
    Returns Shit
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)
help(least_difference)