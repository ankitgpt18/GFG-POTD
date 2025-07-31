class Solution:
    def powerfulInteger(self, intervals, k):
        if not intervals or k <= 0:
            return -1
        
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        events.sort()
        
        max_powerful = -1
        current_count = 0
        prev_pos = None
        
        for pos, delta in events:
            if prev_pos is not None and current_count >= k and prev_pos < pos:
                max_powerful = max(max_powerful, pos - 1)
            
            current_count += delta
            prev_pos = pos
        
        return max_powerful
