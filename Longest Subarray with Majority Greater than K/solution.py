class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        max_len = 0
        sum_map = {0: -1}
        
        for i in range(n):
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            if prefix_sum > 0:
                max_len = i + 1
            else:
                if prefix_sum - 1 in sum_map:
                    max_len = max(max_len, i - sum_map[prefix_sum - 1])
                
                if prefix_sum not in sum_map:
                    sum_map[prefix_sum] = i
        
        return max_len
