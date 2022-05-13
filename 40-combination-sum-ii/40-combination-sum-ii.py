class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(i = 0, current = [], total = 0, nextNum = False):
            
            
            while i > 0 and i < len(candidates) and nextNum and candidates[i] == candidates[i - 1]:
                i += 1
            
            if total == target:
                ans.append(current.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            dfs(i + 1, current, total + candidates[i])
            current.pop()
            dfs(i + 1, current, total, True)
            
            
            
            
            

        dfs()
        return ans