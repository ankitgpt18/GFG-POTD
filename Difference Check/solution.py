class Solution:
    def minDifference(self, arr):
      
        def timeToSeconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        
        seconds = sorted([timeToSeconds(time) for time in arr])
        
        min_diff = float('inf')
        n = len(seconds)
        
        for i in range(n - 1):
            min_diff = min(min_diff, seconds[i + 1] - seconds[i])
        
        wrap_around = 86400 - (seconds[-1] - seconds[0])
        min_diff = min(min_diff, wrap_around)
        
        return min_diff
