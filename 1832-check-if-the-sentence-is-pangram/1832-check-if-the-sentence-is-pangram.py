class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # 26 letter in english
        
        if len(sentence) < 26:
            return False
        
        h_s = {}
        
        for i in range(ord('a'), ord('z') + 1):
            h_s[chr(i)] = False
        
        for val in sentence:
            h_s[val] = True
        
        return False if False in h_s.values() else True
        