class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        
        for i in range(n):
            ans.append([])
            for j in range(n):
                ans[i].append(None)
        
        top, bottom, left, right = 0, n, 0, n
        counter = 1
        while top < bottom and left < right:
            
            for j in range(left, right):
                ans[top][j] = counter
                counter += 1

            for i in range(top + 1, bottom):
                ans[i][right - 1] = counter
                counter += 1
                
            
            for j in range(right - 2, left - 1, -1):
                ans[bottom - 1][j] = counter
                counter += 1
            
            for i in range(bottom - 2, top, -1):
                ans[i][left] = counter
                counter += 1
            #print(ans)
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return ans
        
        
        
        