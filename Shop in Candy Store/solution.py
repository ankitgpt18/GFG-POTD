class Solution:
    def minMaxCandy(self, prices, k):
        n = len(prices)
        prices.sort()
        
        min_cost = 0
        bought = 0
        i = 0
        while bought < n:
            min_cost += prices[i]
            bought += k + 1
            i += 1
        
        max_cost = 0
        bought = 0
        i = n - 1
        while bought < n:
            max_cost += prices[i]
            bought += k + 1
            i -= 1
        
        return [min_cost, max_cost]
