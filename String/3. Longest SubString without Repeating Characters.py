# Given a string s, find the length of the longest substring without repeating characters.

def LenghtOfSubString(s):
    ss = ""
    maxLength = 0
    for c in s:
        lastIndex = ss.find(c)
        if lastIndex > -1:
            ss = ss[lastIndex + 1:]
        ss += c
    return maxLength

print(LenghtOfSubString("pwwkew"))