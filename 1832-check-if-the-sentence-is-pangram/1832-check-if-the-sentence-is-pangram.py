class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 26 letter in english
        
        seen = [False] * (ord('z') + 1 - ord('a'))
        
        for char in sentence:
            seen[ord(char) - ord('a')] = True
            
        return False if False in seen else True
        