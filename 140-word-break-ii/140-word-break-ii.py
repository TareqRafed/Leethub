class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_dict = set(wordDict)
        res = []
        def backtrack(string):
            arr = []
            for i in range(len(string) + 1):
                for val in wordDict:
                    #print(string[0:i], string[i:])
                    if string[0:i] == val:
                        
                        if i == len(string):
                            arr.append(string[0:i])
                            break
                        for val2 in backtrack(string[i:]):
                            arr.append(f'{string[0:i]} {val2}')
                        
                    
            
            #print(arr) 
            return arr
        
        
        return backtrack(s)