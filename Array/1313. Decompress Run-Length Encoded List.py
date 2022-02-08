
def decompress(arr):
    n = len(arr)
    res = []
    for i in range(0,n-1,2):
        for _ in range(arr[i]):
            # print(arr[i])
            print(_)
            res.append(arr[i+1])


    return res


a = [1,2,3,4]

print(decompress(a))