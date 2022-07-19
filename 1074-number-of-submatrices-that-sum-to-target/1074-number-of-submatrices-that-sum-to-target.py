class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        xlen, ylen, ans = len(matrix[0]), len(matrix), 0
        for r in matrix:
            for j in range(1, xlen):
                r[j] += r[j-1]
        for j in range(xlen):
            for k in range(j, xlen):
                res, csum = {0: 1}, 0
                for r in matrix:
                    csum += r[k] - (r[j-1] if j else 0)
                    if csum - target in res: ans += res[csum-target]
                    res[csum] = res[csum] + 1 if csum in res else 1  
        return ans