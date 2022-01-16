
def CheckTwoWords(word1,word2):
    w = set(word1+word2)
    print(w)
    for item in w:

        if abs(word1.count(item) - word2.count(item)) > 3:
            return False
    return True

w1 ="abcdeef"
w2 = "abaaacc"
CheckTwoWords(w1,w2)