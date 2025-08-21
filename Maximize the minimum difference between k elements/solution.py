class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        
        def canSelect(minDiff):
            count = 1
            lastSelected = arr[0]
            
            for i in range(1, n):
                if arr[i] - lastSelected >= minDiff:
                    count += 1
                    lastSelected = arr[i]
                    if count == k:
                        return True
            return False
        
        left, right = 0, arr[-1] - arr[0]
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canSelect(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
