class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        newGoal = word[0]
        rowLen = len(board)
        colLen = len(board[0])
        memo = set()
        def dfs(index = 0, row = 0, col = 0,):
            if index == len(word):
                return True
            
            if row < 0 or col < 0 or row >= rowLen or col >= colLen or board[row][col] != word[index] or (row, col) in memo:
                return False
            
            memo.add((row, col))
            res = (dfs(index + 1, row + 1, col) or
                  dfs(index + 1, row - 1, col) or 
                  dfs(index + 1, row, col + 1) or 
                  dfs(index + 1, row, col - 1) )
            memo.remove((row, col))
            
            return res
        
        for r in range(rowLen):
            for c in range(colLen):
                if dfs(0, r, c): return True
        return False