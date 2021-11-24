
def SortByParity(nums):
    a,b = [],[]

    for i in nums:
        if i%2 == 0:
            a.append(i)
        else:
            b.append(i)

    return a+b


arr = [3,1,2,4]
print(SortByParity(arr))