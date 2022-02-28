
def lengthofLastWord(s):
    lis = list(s.split(" "))

    print(lis)
    s_ = [x for x in lis if len(x.strip()) > 0]
    # print("S:",s_)
    return len(s_[-1])


str = "   fly me   to   the moon  "
print(lengthofLastWord(str))
