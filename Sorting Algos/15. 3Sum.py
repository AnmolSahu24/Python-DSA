
def threeSum(nums):
    nums.sort()
    print(nums)
    ans = set()

    for i,v in enumerate(nums):
        # print(" i:",i,"\n","v:",v)
        twoSum(nums[i+1:],-v,ans)
    return ans

def twoSum(nums,target,ans):
    d = {}

    for i,v in enumerate(nums):
        if target-v in d:
            ans.add((v,target-v,-target))
        d[v]=i


num = [-1,0,1,2,-1,-4]
print(threeSum(num))