
def RemoveDuplicate(nums):
    if len(nums) == 0: return 0
    # The first value in the array will be unique, so we can ignore it.
    retLen = 1
    for i in range(1, len(nums)):
        print("i", i)
        # Spotted a unique, change the element at the
        # retLen index before incrementing it.
        if nums[i - 1] != nums[i]:
            # nums[retLen] = nums[i]
            retLen += 1
    return retLen




a = [0,0,1,1,1,2,2,3,3,4]
print(RemoveDuplicate(a))