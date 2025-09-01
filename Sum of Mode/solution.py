class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        freq = {}
        result = 0
        
        for i in range(n - k + 1):
            if i == 0:
                for j in range(k):
                    freq[arr[j]] = freq.get(arr[j], 0) + 1
            else:
                freq[arr[i + k - 1]] = freq.get(arr[i + k - 1], 0) + 1
                freq[arr[i - 1]] -= 1
                if freq[arr[i - 1]] == 0:
                    del freq[arr[i - 1]]
            
            max_freq = 0
            mode = float('inf')
            for num, f in freq.items():
                if f > max_freq or (f == max_freq and num < mode):
                    max_freq = f
                    mode = num
            
            result += mode
        
        return result
