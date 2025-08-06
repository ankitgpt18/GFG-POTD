class Solution:
    def romanToDecimal(self, s): 
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            current_value = roman_values[s[i]]
            
            if i < n - 1 and current_value < roman_values[s[i + 1]]:
                result -= current_value
            else:
                result += current_value
        
        return result
