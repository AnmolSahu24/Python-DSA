
def heightChecker(height):
    sortH = sorted(height)
    print(sortH)
    c = 0
    for i in range(len(height)):
        print("h:",height[i],"H:",sortH[i])
        if height[i] != sortH[i]:
            print("Boyah!")
            c+=1

    return c

h = [1,1,4,2,1,3]
[1, 1, 1, 2, 3, 4]
print(heightChecker(h))