
def letterCombination(digit):

    number_to_char = {
        "1" : [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", 'y', "z"]
    }

    if len(digit) == 0:
        return []

    elif len(digit) ==1:
        return number_to_char[digit]

    else:
        res  = []

        prefixes = number_to_char[digit[0]]
        # sufixes = self.letterCombinations(digits[1:])
        sufixes = number_to_char[digit[1:]]

        for pre in prefixes:
            for suf in sufixes:
                res.append(pre+suf)

        return res



print(letterCombination("17"))