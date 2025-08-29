class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1
        
        required = len(p_count)
        formed = 0
        window_counts = {}
        
        left = right = 0
        min_len = float('inf')
        min_left = 0
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in p_count and window_counts[char] == p_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                window_counts[char] -= 1
                if char in p_count and window_counts[char] < p_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
