
def Shuffle(nums,n):
    k = []
    for i in range(len(nums)):
        print(i)
        print("--",i+n)
        if i + n <= len(nums) - 1:
            k.append(nums[i])
            print("-->",k)
            k.append(nums[i + n])
            print("==>",k)
    return k


num = [2,5,1,3,4,7]
n =3
print(Shuffle(num,n))