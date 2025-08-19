class Solution:
    def farMin(self, arr):
        n = len(arr)
        ans = [-1] * n
        
        min_arr = [0] * n
        min_arr[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            min_arr[i] = min(arr[i], min_arr[i+1])
        
        for i in range(n):
            l, h, res = i+1, n-1, -1
            
            while l <= h:
                mid = (l + h) // 2
                if min_arr[mid] < arr[i]:
                    res = mid
                    l = mid + 1
                else:
                    h = mid - 1
            
            ans[i] = res
        
        return ans
