class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        string = ''
        for i, val in enumerate(s):
            if val == ' ':
                continue
            else:
                string = s[i:]
                break
        if not string:
            return 0
        isMinus = string[0] == '-'
        if string[0] == '-' or string[0] == '+':
            string = string[1:]
        numStr = ''
        for val in string:
            if val.isnumeric():
                numStr += val
            else:
                break
        if not numStr:
            return 0
        ans = int(numStr)
        if ans.bit_length() >= 32:
            ans = 1 << 32
            ans = ans // 2
            if not isMinus:
                ans -= 1
        if isMinus:
            return -1 * ans
        
        return ans