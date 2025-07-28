class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        target_sum = max(max(row_sums), max(col_sums))
        
        operations = 0
        
        for i in range(n):
            for j in range(n):
                row_deficit = target_sum - row_sums[i]
                col_deficit = target_sum - col_sums[j]
                
                increment = min(row_deficit, col_deficit)
                
                if increment > 0:
                    operations += increment
                    mat[i][j] += increment
                    row_sums[i] += increment
                    col_sums[j] += increment
        
        return operations
