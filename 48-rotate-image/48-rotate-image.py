class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixLen = len(matrix)
        for i, row in enumerate(matrix):
            for reversedRow in reversed(matrix):
                row.append(reversedRow[i])
        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][matrixLen:]
        
        