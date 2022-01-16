def MaxNoWords(str):
    arr = []
    for i in str:
        # print(i)
        x = i.split(" ")
        # print(len(x))
        arr.append(len(x))

        # print(arr)

    return max(arr)



x = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(MaxNoWords(x))