
def Majority(nums):
    majority = {}
    for k in nums:
        if k in majority:
            majority[k] +=1
        else:
            majority[k]=1

    for k in majority:
        maj_key = max(majority,key = majority.get)
        print("Anmol")
        return maj_key


arr = [3,2,3,2]
print(Majority(arr))

