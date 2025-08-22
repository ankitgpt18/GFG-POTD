class Solution:
    def median(self, mat):
        n, m = len(mat), len(mat[0])
        low, high = mat[0][0], mat[0][m-1]
        
        for i in range(1, n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][m-1])
        
        desired = (n * m + 1) // 2
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for i in range(n):
                count += self.countSmallerEqual(mat[i], mid)
            
            if count < desired:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    def countSmallerEqual(self, row, x):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        return left
