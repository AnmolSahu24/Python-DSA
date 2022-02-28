
def reverseStr(s,k):
    op = []
    for i in range(0, len(s), 2 * k):
        op.append(s[i:k + i][::-1])
        op.append(s[k + i:i + (2 * k)])
    return "".join(op)

str = "abcdefg"
k = 2
print(reverseStr(str,k=k))