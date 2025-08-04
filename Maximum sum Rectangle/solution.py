class Solution:
    def maxRectSum(self, mat):
        n = len(mat)
        m = len(mat[0])
        finalmaxi = float('-inf')
        
        for s in range(m):
            temp = [0] * n
            for e in range(s, m):
                for i in range(n):
                    temp[i] += mat[i][e]
                
                sum_val = 0
                maxi = float('-inf')
                for i in range(n):
                    sum_val += temp[i]
                    maxi = max(maxi, sum_val)
                    if sum_val < 0:
                        sum_val = 0
                
                finalmaxi = max(finalmaxi, maxi)
        
        return finalmaxi
