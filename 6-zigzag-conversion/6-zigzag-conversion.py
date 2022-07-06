class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        ans = ''
        
        if numRows == 1:
            return s
        
        def dfs(currIndex, arr):
            if currIndex >= len(s):
                return arr
            row = 0
            for j in range(currIndex, currIndex + numRows):
                if j >= len(s):
                    break
                arr[row].append(s[j])
                row += 1

            row = numRows - 2
            for k in range(currIndex + numRows, currIndex + (numRows * 2) - 2):
                if k >= len(s):
                    break
                arr[row].append(s[k])
                row -= 1
            
            return dfs(currIndex + (numRows * 2) - 2, arr)
        
        zigzag = [[] for _ in range(numRows)] 
        
        zigzag = dfs(0, zigzag)
        
        for row in zigzag:
            for letter in row:
                ans += letter
        
        return ans
