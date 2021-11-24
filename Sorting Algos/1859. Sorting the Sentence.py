
def sortSentence(s):
    # buffer = [''] * (len(s))
    #
    # s = s.split(' ')
    # print(s)
    #
    # for word in s:
    #     word = list(word)
    #     print("--",word)
    #     index = int(word.pop()) -1 # to get the last element of the string
    #     print(index)
    #     buffer[index] = "".join(word)
    #
    # return " ".join(buffer)
    arr_len = s.split()
    res = [None] * len(arr_len)
    for i in arr_len:
        res[int(i[-1]) - 1] = i[:-1]
    return ' '.join(res)
sent = "is2 sentence4 This1 a3"
print(sortSentence(sent))