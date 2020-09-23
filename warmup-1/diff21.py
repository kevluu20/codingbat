def diff21(n):
    """return difference of 21 or if greater, then differece * 2"""
    if n <= 21:
        return (21 - n)
    else:
        return (n - 21) * 2


print(diff21(22))
