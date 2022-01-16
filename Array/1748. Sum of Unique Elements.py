
from typing import Counter

def SumOfUnique(arr):

    sum = 0

    helper = set(arr)

    for i in helper:
        print(arr.count(i))
        if arr.count(i) == 1:
            sum +=i
    return sum



arr = [1,2,3,2]
print(SumOfUnique(arr))