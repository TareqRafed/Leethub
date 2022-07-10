class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev, dic = 0, 0, { 
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        for i in s[::-1]:
            if dic[i] >= prev:
                res += dic[i]
            else:
                res -= dic[i]
            prev = dic[i]
        return res
