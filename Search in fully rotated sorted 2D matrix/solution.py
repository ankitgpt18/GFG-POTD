class Solution:
    def searchMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        left, right = 0, n * m - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, m)
            mid_val = mat[row][col]
            
            if mid_val == x:
                return True
            
            start_val = mat[0][0]
            end_val = mat[n-1][m-1]
            
            if start_val <= end_val:
                if x < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid_val >= start_val:
                    if x >= start_val and x < mid_val:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if x <= end_val and x > mid_val:
                        left = mid + 1
                    else:
                        right = mid - 1
        
        return False
