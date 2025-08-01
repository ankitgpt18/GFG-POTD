class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        n = len(arr)
        
        prefix = [0]
        for s in arr:
            balance = 0
            for char in s:
                if char in vowels:
                    balance += 1
                else:
                    balance -= 1
            prefix.append(prefix[-1] + balance)
        
        count = 0
        balance_count = {}
        
        for balance in prefix:
            if balance in balance_count:
                count += balance_count[balance]
                balance_count[balance] += 1
            else:
                balance_count[balance] = 1
        
        return count
