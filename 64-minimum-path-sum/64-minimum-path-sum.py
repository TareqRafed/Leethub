class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        
        cache = {}
        
        def dfs(row, col, a):
            
            # check cache first
            if f'{row}, {col}' in cache:
                return cache[f'{row}, {col}'] + a
            
            # Base Case
            if row == rowLen - 1 and col == colLen - 1:
                return a + grid[row][col]
            
            
            
            # edges
            if row == rowLen - 1:
                cache[f'{row}, {col}'] = dfs(row, col + 1, grid[row][col])
                return cache[f'{row}, {col}']  + a
            if col == colLen - 1:
                cache[f'{row}, {col}'] = dfs(row + 1, col, grid[row][col])
                return cache[f'{row}, {col}']  + a
            
            
            
           
            # non edges
            
            
            sumR = dfs(row + 1, col, grid[row][col])
            sumC = dfs(row, col + 1, grid[row][col])

            cache[f'{row}, {col}'] = min(sumR, sumC)
            return cache[f'{row}, {col}'] + a
    
        return dfs(0,0,0)
            
            
            