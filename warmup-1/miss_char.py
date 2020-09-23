def missing_char(str, n):
    """removing letter from a word"""
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back


print(missing_char('kitten', 1))
