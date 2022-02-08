def maxSubArray(nums):

    maxSum = sum(nums)
    sumArray = 0

    for num in nums:
        sumArray += num
        print(sumArray)

        if(sumArray > maxSum):
            maxSum = sumArray

        if(sumArray<0):
            sumArray = 0

    return maxSum








arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(arr))