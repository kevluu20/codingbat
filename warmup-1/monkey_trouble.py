def monkey_trouble(a_smile, b_smile):
    """changing True/False depending if 2 monkeys are smiling or not"""
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    else:
        return False


print(monkey_trouble(False, True))
