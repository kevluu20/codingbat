def near_hundred(n):
    """True if within 10 of 100 or 200"""
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


print(near_hundred(95))
