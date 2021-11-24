def subtractProductAndSum( n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    mul = 1
    for i in str(n):
        sum += int(i)
        mul = mul * int(i)
    return mul - sum


print(subtractProductAndSum(234))