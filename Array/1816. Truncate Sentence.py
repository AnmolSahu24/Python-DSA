
def TruncateSentance(str,k):
    string_ = list(str.split(" "))
    print(" ".join(string_[:k]))
    return " ".join(string_[:k])


TruncateSentance("Hello how are you Contestant",4)

