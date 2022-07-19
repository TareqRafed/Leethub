class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        @cache
        def dfs(i):
            
            if i == 1:
                return [1]
            
            arr = [1 for _ in range(i)]
            
            if len(arr) == 2:
                return arr
            
            n_a = dfs(i - 1)
            for j in range(1, i - 1):
                arr[j] = n_a[j] + n_a[j - 1]
            
            return arr
        
        for i in range(1, numRows + 1):
            ans.append(dfs(i))
        
        return ans