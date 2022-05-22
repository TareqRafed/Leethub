class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS_LEN = len(board)
        COL_LEN = len(board[0])
        
        path = set()
        
        def dfs(row, col, index):
            if index == len(word):
                return True
        
            if (row >= ROWS_LEN 
            or col >= COL_LEN 
            or row < 0 
            or col < 0 
            or board[row][col] != word[index]
            or (row, col) in path):
                return False
            
            path.add((row, col))
            
            res = (dfs(row + 1, col, index + 1) or
                  dfs(row - 1, col, index + 1) or
                  dfs(row, col + 1, index + 1) or
                  dfs(row, col - 1, index + 1))
            
            path.remove((row, col))
            
            return res
        
        for row in range(ROWS_LEN):
            for col in range(COL_LEN):
                if dfs(row, col, 0): return True
        
        return False
    

