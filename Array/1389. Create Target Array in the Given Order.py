def creatTarget (nums, index):
    n = len(nums)
    res = []
    i = 0
    while i < n:
            res.insert(index[i], nums[i])

            i+=1
    return res


nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(creatTarget(nums,index))