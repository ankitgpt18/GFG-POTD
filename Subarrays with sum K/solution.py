class Solution:
    def cntSubarrays(self, arr, k):
        count = 0
        prefix_sum = 0
        sum_map = {0: 1}
        
        for num in arr:
            prefix_sum += num
            
            if (prefix_sum - k) in sum_map:
                count += sum_map[prefix_sum - k]
            
            if prefix_sum in sum_map:
                sum_map[prefix_sum] += 1
            else:
                sum_map[prefix_sum] = 1
        
        return count
