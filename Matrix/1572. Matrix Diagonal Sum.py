
def DiagonalSum(mat):
    cumsum = 0
    for i in range(len(mat)):
        if i == len(mat)-i-1:
            cumsum +=mat[i][i]
        else:
            cumsum += (mat[i][i] + mat[i][len(mat)-i-1])

    return cumsum




# matrix = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
matrix = [[1,2,3],
            [4,5,6],
              [7,8,9]]
print(DiagonalSum(matrix))