class Solution:
    def countValid(self, n, arr):
        required = set(arr)
        available = [i for i in range(10) if i not in required]
        
        if not available:
            return 9 * (10 ** (n - 1)) if n > 1 else 9
        
        def count_without():
            if n == 1:
                return len([d for d in available if d != 0])
            
            first_pos = len([d for d in available if d != 0])
            remaining_pos = len(available) ** (n - 1)
            return first_pos * remaining_pos
        
        total = 9 * (10 ** (n - 1)) if n > 1 else 9
        return total - count_without()
