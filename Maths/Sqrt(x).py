
def Sqrt(x):
    # count = 0
    #
    # for i in range(1,x+1,2):
    #     x -= i
    #
    #     if x >= 0:
    #         count +=1
    #     elif x<0:
    #         break
    # return count
    ans = 0
    while ans * ans <= x:
        print("--",ans)

        ans += 1
        print(ans)
    return ans - 1

print(Sqrt(25))
