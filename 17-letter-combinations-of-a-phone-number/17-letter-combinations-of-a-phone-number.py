class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numpad = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        ans = []
        
        if len(digits) == 0:
            return ans
        
        def dfs(i, string):
            
            if i == len(digits):
                return ans.append(string)
            arr = []
            for val in numpad[int(digits[i])]:
                dfs(i + 1, string + val)

        
        dfs(0, '')
        return ans