def printsnake(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if i %2 ==  0 :
            for j in range(col):
                print(matrix[i][j],end= " ")
            print()
        else:
            for j in range(col-1 , -1, - 1):
                print(matrix[i][j],end= " ")
            print()




matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

printsnake(matrix)
