class Solution:
    def numberOfWays(self, s: str) -> int:
         
        counting = defaultdict(int)
        for val in s:
            counting[val] += 1

        ones = counting['1']
        zeros = counting['0']

        beforeCounter = {
            '0': 0,
            '1': 0
        }
        res = 0
        for string in s:
            if string == '0':
                onesBefore = beforeCounter['1']
                onesAfter = ones - onesBefore
                res += onesBefore * onesAfter
                beforeCounter['0'] += 1
               
            else:
                zerosBefore = beforeCounter['0']
                zerosAfter = zeros - zerosBefore
                res += zerosBefore * zerosAfter
                beforeCounter['1'] += 1

        return res