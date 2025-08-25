class Solution:
   def possible(self, mid, arr, k):
       val = 0
       n = len(arr)
       half = n // 2
       if n % 2 == 0:
           val += max(0, 2 * mid - arr[half] - arr[half - 1])
       else:
           val += max(0, mid - arr[half])
       for i in range(half + 1, n):
           val += max(0, mid - arr[i])
       return val <= k
   
   def maximizeMedian(self, arr, k):
       arr.sort()
       l = 0
       r = arr[-1] + k
       ans = 0
       while l <= r:
           mid = l + (r - l) // 2
           if self.possible(mid, arr, k):
               ans = mid
               l = mid + 1
           else:
               r = mid - 1
       return ans
