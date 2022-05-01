class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        trianHeight = len(triangle)
        lastColInd = len(triangle[-1]) - 1
        def minSum(self, row, col):
            key = f'{row}, {col}'
            
            if row > (trianHeight - 1):
                return 0
            
            if row + 1 < trianHeight and col < len(triangle[row]):
                triangle[row][col] = min(triangle[row][col] + triangle[row + 1][col + 1], triangle[row][col] + triangle[row + 1][col])
            else:
                pass
            
            if row == 0 == col:
                return triangle[row][col]
            
            if col + 1 >= len(triangle[row]):
                return minSum(self, row - 1, 0)
            else:
                return minSum(self, row, col + 1)
            
        
        return minSum(self, trianHeight - 1, 0)
            