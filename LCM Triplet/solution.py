class Solution:
    def lcmTriplets(self, n):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def lcm_three(a, b, c):
            return lcm(lcm(a, b), c)
        
        if n <= 2:
            return n
        if n == 3:
            return 6
        
        if n % 2 == 1:
            return lcm_three(n, n-1, n-2)
        else:
            if n % 3 == 0:
                return lcm_three(n-1, n-2, n-3)
            else:
                return lcm_three(n, n-1, n-3)
