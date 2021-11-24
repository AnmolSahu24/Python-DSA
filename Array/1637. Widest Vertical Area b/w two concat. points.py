
def maxWidthofVerticalArea(points):

    L,max = [],0

    for i in range(len(points)):
        # print(i)
        L.append(points[i][0])
        # print(L)
        L = list(set(L))
        L.sort()

    for i in range(len(L)-1):
        # print(i)
        if L[i+1] - L[i] > max:
            max = L[i+1] - L[i]

    return max

pts = [[8,7],[9,9],[7,4],[9,7]]
maxWidthofVerticalArea(pts)
print(maxWidthofVerticalArea(pts))