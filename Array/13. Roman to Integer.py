

def romantoInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res = 0

    for char in s:
        res += roman_dict[char]

    return res

print(romantoInt("III"))