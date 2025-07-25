class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        
        def kadane_max(arr):
            max_ending_here = max_so_far = arr[0]
            for i in range(1, n):
                max_ending_here = max(arr[i], max_ending_here + arr[i])
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        def kadane_min(arr):
            min_ending_here = min_so_far = arr[0]
            for i in range(1, n):
                min_ending_here = min(arr[i], min_ending_here + arr[i])
                min_so_far = min(min_so_far, min_ending_here)
            return min_so_far
        
        max_kadane = kadane_max(arr)
        min_kadane = kadane_min(arr)
        total_sum = sum(arr)
        
        if total_sum == min_kadane:
            return max_kadane
        
        max_circular = total_sum - min_kadane
        
        return max(max_kadane, max_circular)
