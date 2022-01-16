def atoi(s):
    s = s.strip()
    n = len(s)
    isPositive = True

    if ( n > 0):

        if(s[0] == "-"):

            isPositive = False
            s = s[1:]
            print(s)

    elif(s[0] == "+"):
        s = s[1:]

    for i,c in enumerate(s):
        print(i,c)
        if(not c.isdigit()):
            s = s[:i]

    if(len(s) > 0):
        if(not isPositive):
            print("b",s)

            s = int(s) * -1
            print("boo",s)
        else:
            s = int(s)
    else:
        return 0

    min = -2147483648
    max = 2147483647
    if (s > max):
        s = max
    elif (s < min):
        s = min

    return s

print(atoi("  -321"))
