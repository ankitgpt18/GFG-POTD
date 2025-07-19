class Solution:
    def vowelCount(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowel_counts = {}
        
        for char in s:
            if char in vowels:
                vowel_counts[char] = vowel_counts.get(char, 0) + 1
        
        unique_vowel_count = len(vowel_counts)
        
        if unique_vowel_count == 0:
            return 0
        
        factorial = 1
        for i in range(1, unique_vowel_count + 1):
            factorial *= i
        
        total_combinations = 1
        for count in vowel_counts.values():
            total_combinations *= count
        
        return total_combinations * factorial
