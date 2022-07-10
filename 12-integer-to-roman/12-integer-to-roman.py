class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        ans = ''
        totalDigits = len(str(num))
        for i, numStr in enumerate(str(num)):
            if numStr == '0':
                continue
            num = int(numStr) * (10 ** (totalDigits - (i + 1)) )
            soloNum = int(numStr)
            tens = num // soloNum
            if 1 < soloNum <= 3:
                for i in range(soloNum):
                    ans += dic[tens]
            
            elif soloNum == 4 or soloNum == 9:
                temp = soloNum
                sRoman = dic[1 * tens]
                bRoman = dic[(soloNum + 1) * tens]

                ans += sRoman
                ans += bRoman
            
            elif 6 <= soloNum <= 8:
                ans += dic[5 * tens]
                for i in range(soloNum - 5):
                    ans += dic[tens]
            else:
                ans += dic[num]
        return ans