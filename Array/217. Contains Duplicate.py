def containsduplicate(nums):
    nums.sort()
    flag = False
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i + 1]):
            flag = True
            return flag
    return flag



ar = [1,2,3,1]
print(containsduplicate(ar))
