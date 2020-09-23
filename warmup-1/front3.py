def front3(str):
    """Repeat first 3 letters 3 times"""
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front + front + front
