
def str (strs):
    res = ""
    print(len(strs[0]))

    for i in range(len(strs[0])):
        print(i)
        for s in strs:
            print("S:",s)
            print("s[i]",s[i])
            print("strs[0][i]",strs[0][i])
            if i == len(s) or s[i] != strs[0][i]:
                return res


a = ["flower","flow","flight"]
str(a)