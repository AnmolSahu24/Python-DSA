
from collections import Counter

def topKfrequest(nums,k):
    count = Counter(nums)
    print(count)
    res = []

    for pair in count.most_common(1):
        print(pair)
        res.append(pair[0])

    return res



arr =  [1,1,1,2,2,3,4,4,4,4]
k = 2
print(topKfrequest(arr,k))