
def ArrayPartition(nums):
    nums  = sorted(nums,reverse = True)

    newlist = []
    print(nums)
    for x in range(0,len(nums),2):
        print(x)
        print(nums[x:x+2])
        newlist.append(min(nums[x:x+2]))

    print("--",newlist)
    print("++",sum(newlist))
    return sum(newlist)

ArrayPartition([6,2,6,5,1,2])