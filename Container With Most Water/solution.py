class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            area = width * height
            max_area = max(max_area, area)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
