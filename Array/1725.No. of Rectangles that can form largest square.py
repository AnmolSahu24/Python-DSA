
def CountRectangles(rectangles):

    s_d = []

    for l,w in rectangles:
        s_d.append(min(l,w))

    maxLen = max(s_d)
    count = 0

    for d in s_d:
        if d == maxLen:
            count +=1
    return count


rect = [[5,8],[3,9],[5,12],[16,5]]
print(CountRectangles(rect))