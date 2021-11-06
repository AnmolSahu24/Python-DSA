
def ReverseInt(x):

    res = int(str(x)[::-1]) if x >0 else int(str(x)[:0:-1])*-1

    if 2**31-1 > res > -2**31:
        return res

    else:
        return 0


print(ReverseInt(-258))