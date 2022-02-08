def rightRotateByOne(nums,k):
    print(nums)
    for i in range(k):
        nums.insert(0, nums[-1])
        nums.pop(-1)
    print(nums)
arr = [ 1, 2, 3, 4, 5 ]
lenth = len(arr)
K = 2

print(rightRotateByOne(arr,K))

[ 4,5, 2, 3,  ]