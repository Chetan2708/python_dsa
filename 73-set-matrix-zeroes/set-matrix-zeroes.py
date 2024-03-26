class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(mat)
        cols = len(mat[0])

        rowArray = [0]* rows
        colsArray = [0]* cols

        for i in range(rows):
            for j in range(cols):
                if not mat[i][j]:  #If zero is found
                    rowArray[i] = 1
                    colsArray[j] =1
                
        for i in range(rows):
            for j in range(cols):
                if rowArray[i] or colsArray[j]:
                    mat[i][j] = 0

