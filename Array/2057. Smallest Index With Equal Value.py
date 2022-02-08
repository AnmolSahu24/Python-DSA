
def smallestIndx(nums):
    for idx, n in enumerate(nums):
        if idx % 10 == n:
            return idx
    return -1 
