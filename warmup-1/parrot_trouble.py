def parrot_trouble(talking, hour):
    """If parrot talking between 7 and 20, true and in trouble"""
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False
