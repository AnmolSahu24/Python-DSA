
def KidsWithCandies(candList, extra):
    max_ = max(candList)
    res = [False] * len(candList)
    for idx, candy in enumerate(candList):
        if candy + extra >= max_:
            res[idx] = True
        # else:
        #     res.append(False)

    return res

arr = [2,3,5,1,3]
ext = 3
print(KidsWithCandies(arr,ext))