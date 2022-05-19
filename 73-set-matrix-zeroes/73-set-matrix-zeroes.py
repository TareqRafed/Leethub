class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        def clearRowCol(row, col):
            for i in range(colLen):
                if matrix[row][i] != 0:
                    matrix[row][i] = 'x'
            for i in range(rowLen):
                if matrix[i][col] != 0:
                    matrix[i][col] = 'x'
        
        for row in range(rowLen):
            for col in range(colLen):
                if matrix[row][col] == 0:
                    clearRowCol(row, col)
        
        for row in range(rowLen):
            for col in range(colLen):
                if matrix[row][col] == 'x':
                    matrix[row][col] = 0
                
        