class Solution:
    def numTrees(self, n: int) -> int:
        g_array = [1,1]
        
        for j in range(2,n+1):
            sum_g = 0
            for i in range(1,j+1):
                f_i = g_array[i-1]*g_array[j-i]
                sum_g += f_i
            g_array.append(sum_g)
                        
        return g_array[n]