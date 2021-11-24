
def smallerThanCurrent(arr):
    lst = list(sorted(arr))
    print(lst)
    print(lst.index(i) for i in arr)
    return [lst.index(i) for i in arr]


print((smallerThanCurrent([8,1,2,2,3])))