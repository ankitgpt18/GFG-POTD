class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])
        
        diff = [[0] * (m + 1) for _ in range(n + 1)]
        
        for op in opr:
            val = op[0]
            r1 = op[1]
            c1 = op[2]
            r2 = op[3]
            c2 = op[4]
            
            diff[r1][c1] += val
            if c2 + 1 < m:
                diff[r1][c2 + 1] -= val
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= val
            if r2 + 1 < n and c2 + 1 < m:
                diff[r2 + 1][c2 + 1] += val
        
        for i in range(n):
            for j in range(m):
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
        
        for j in range(m):
            for i in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
        
        result = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(mat[i][j] + diff[i][j])
            result.append(row)
        
        return result
