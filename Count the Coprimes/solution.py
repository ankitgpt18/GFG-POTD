from array import array
from math import isqrt

class Solution:
    def cntCoprime(self, arr):
        MAX = max(arr)
        freq = array('i', [0] * (MAX + 1))
        for num in arr:
            freq[num] += 1

        mobius = array('i', [1] * (MAX + 1))
        is_prime = array('b', [1] * (MAX + 1))

        for i in range(2, MAX + 1):
            if is_prime[i]:
                for j in range(i, MAX + 1, i):
                    mobius[j] *= -1
                    is_prime[j] = 0
                for j in range(i * i, MAX + 1, i * i):
                    mobius[j] = 0

        divisible_count = array('i', [0] * (MAX + 1))
        for num in range(1, MAX + 1):
            if freq[num]:
                for d in range(1, isqrt(num) + 1):
                    if num % d == 0:
                        divisible_count[d] += freq[num]
                        if d != num // d:
                            divisible_count[num // d] += freq[num]

        total = 0
        for d in range(1, MAX + 1):
            count = divisible_count[d]
            total += mobius[d] * count * (count - 1) // 2

        return total
