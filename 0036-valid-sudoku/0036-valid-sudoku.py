class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    num = board[i][j]
                    in_row = num + f'in {i}r'
                    in_col = num + f'in {j}c'
                    in_box = num + f'box: {i//3} {j//3}'
                    
                    if in_row in visited \
                    or in_col in visited \
                    or in_box in visited:
                        return False
                    else:
                        visited.add(in_row)
                        visited.add(in_col)
                        visited.add(in_box)
        
        return True