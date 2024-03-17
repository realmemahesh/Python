def rotate(matrix):
    # TODO
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            # coverting row to column, column to row
            #matrix[0][0,1,2],matrix[0,1,2][0] = matrix[0,1,2][0], matrix[0][0,1,2]
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
        
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))