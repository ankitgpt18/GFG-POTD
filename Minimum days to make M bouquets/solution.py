class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        if m * k > n:
            return -1
        
        def canMakeBouquets(days):
            bouquets = 0
            consecutive = 0
            
            for bloom_day in arr:
                if bloom_day <= days:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            
            return bouquets >= m
        
        left, right = min(arr), max(arr)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
