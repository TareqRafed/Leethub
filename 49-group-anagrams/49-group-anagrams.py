class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for val in strs:
            count = [0] * 26
            
            for letter in val:
                count[ord(letter) - ord('a')] += 1
            
            hmap[tuple(count)].append(val)
        
        return hmap.values()
        