
def Kweakest(mat, k):
    hashtable = {}
    res = []
    for i in range(len(mat)):
        # print(i)
        count = mat[i].count(1)
        print(count)
        # Not able to understand the test case covered in this line
        if count not in hashtable.keys():
            hashtable[count] = [i]
            print("XX",hashtable[count],[i])
        else:
            hashtable[count].append(i)
            print(hashtable[count])

    for i in sorted(hashtable.keys()):
            res += hashtable[i]
        #     print(mat[j].count())
    return res[:k]



arr = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

print(Kweakest(arr,3))