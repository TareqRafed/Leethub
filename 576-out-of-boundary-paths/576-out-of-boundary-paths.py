class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        rows = m - 1
        columns = n - 1

        @cache
        def dfs(i, j, moves):
            if moves > maxMove:
                return 0
            
            if i > rows or j > columns or i < 0 or j < 0:
                return 1
            
            count = 0
            count += dfs(i + 1, j, moves + 1)
            count += dfs(i, j + 1, moves + 1)
            count += dfs(i - 1, j, moves + 1)
            count += dfs(i, j - 1, moves + 1)
            
            return count
        
        return dfs(startRow, startColumn, 0) % (10 ** 9 + 7)