def MedianOfTwoSortedArrays(n1,n2):
    concacatArr = sorted(n1+n2)
    n = len(concacatArr)

    if n % 2 ==0:
        z = n //2
        e = concacatArr[z]
        q = concacatArr[z-1]

        ans = (e + q )/2
        print(ans)
        return ans

    else:
        z = n //2
        ans = concacatArr[z]
        print(ans)
        return ans

nums1 = [ -5, 3, 6, 12, 15 ]
nums2 =  [ -12, -10, -6, -3, 4, 10 ]
MedianOfTwoSortedArrays(nums1,nums2)

