class Solution:
    def countNumbers(self, N):
        c = 0
        limit = int(N**0.5)
        prime = [0] * (limit + 1)
        
        for i in range(1, limit + 1):
            prime[i] = i
        
        for i in range(2, int(limit**0.5) + 1):
            if prime[i] == i:
                for j in range(i * i, limit + 1, i):
                    if prime[j] == j:
                        prime[j] = i
        
        for i in range(2, limit + 1):
            p = prime[i]
            q = prime[i // prime[i]]
            if p * q == i and q != 1 and p != q:
                c += 1
            elif prime[i] == i:
                if i**8 <= N:
                    c += 1
        
        return c
