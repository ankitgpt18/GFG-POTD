class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        
        def canAllocate(maxPages):
            students = 1
            currentPages = 0
            
            for pages in arr:
                if pages > maxPages:
                    return False
                if currentPages + pages > maxPages:
                    students += 1
                    currentPages = pages
                    if students > k:
                        return False
                else:
                    currentPages += pages
            
            return True
        
        left = max(arr)
        right = sum(arr)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canAllocate(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
