def front_back(str):
    """return new string with first and last letters switched"""
    if len(str) <= 1:
        return str

    mid = str[1:len(str)-1]

    return str[len(str)-1] + mid + str[0]


print(front_back('Chocolate'))
