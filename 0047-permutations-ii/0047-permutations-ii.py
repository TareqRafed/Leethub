class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(comb.copy())
                return
            
            prev = None
            
            for i, val in enumerate(counter.keys()):
                if counter[val] == 0:
                    continue
                
                comb.append(val)
                counter[val] -= 1
                
                backtrack(comb, counter)
                
                comb.pop()
                counter[val] += 1
                
                
            
            

        backtrack([], Counter(nums))

        return results
            