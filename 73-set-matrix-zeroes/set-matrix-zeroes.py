class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = matrix
        m = matrix[0]
        rowZero = True

        # Traverse and mark first row and first column 
        for i in range(len(n)):
            for j in range(len(m)):
                if matrix[i][j]== 0 :
                    matrix[0][j] = 0 
                
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = False
        # mark the the whole matrix according to first row and column set earlier .. Start from 1st row and column because 1 box has already defined for zeroth row
    
        for i in range(1, len(n)):
            for j in range(1 , len(m)):
                if matrix[0][j] == 0 or matrix[i][0]  == 0:
                    matrix[i][j]= 0

# If 1st is zero then all rows = 0 
        if matrix[0][0] == 0 :
            for i in range(len(n)):
                matrix[i][0] = 0 
 # If 1st is zero then all cols = 0        
        if not rowZero :
            for j in range(len(m)):
                matrix[0][j] = 0 
    

