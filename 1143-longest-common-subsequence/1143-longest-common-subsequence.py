class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        visited = {}

        def dfs(i, j):
            key = f'{i}, {j}'
            if key in visited:
                return visited[key]

            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                visited[key] = dfs(i + 1, j + 1) + 1
            else:
                visited[key] = max(dfs(i, j + 1), dfs(i + 1, j))
            
            return visited[key]


        
        return dfs(0, 0)