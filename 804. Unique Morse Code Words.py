code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
        ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


def UniqueCode(words):
    unique_code = set()
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))
        # print(, end=" ")

    alpha_dict = dict(zip(alphabet, code))
    # print(alpha_dict)

    for j in words:
        # print("----------")
        # print(translate(j))
        unique_code.add(translate(j))
    # print(len(unique_code))
    return len(unique_code)


def translate(word):
    l = list(word)
    # print(l)
    word_dict = dict(zip(l, code))
    # print("".join(word_dict.values()))
    return ("".join(word_dict.values()))


print(UniqueCode(["gin", "zen", "gig", "msg"]))
print(UniqueCode(["a"]))

# translate("gin")
