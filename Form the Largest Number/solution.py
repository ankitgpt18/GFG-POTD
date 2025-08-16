from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        str_arr = [str(num) for num in arr]
        str_arr.sort(key=cmp_to_key(compare))
        result = ''.join(str_arr)
        
        return '0' if result[0] == '0' else result
