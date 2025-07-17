class Solution:
    def maxKPower(self, n, k):
        def prime_factors(num):
            factors = {}
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    num //= d
                d += 1
            if num > 1:
                factors[num] = factors.get(num, 0) + 1
            return factors
        
        def count_prime_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count
        
        k_factors = prime_factors(k)
        min_power = float('inf')
        
        for prime, exp in k_factors.items():
            factorial_count = count_prime_in_factorial(n, prime)
            min_power = min(min_power, factorial_count // exp)
        
        return min_power
