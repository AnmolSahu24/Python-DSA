
def replaceDigits(s):
    string = ''
    for i in range(len(s)):
        if s[i].isnumeric():
            string += chr(ord(s[i - 1]) + int(s[i]))
        else:
            string += s[i]
    return string


s = "a1c1e1"
print(replaceDigits(s))