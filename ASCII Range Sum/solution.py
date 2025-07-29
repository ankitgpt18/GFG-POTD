class Solution:
    def asciirange(self, s):
        first_pos = {}
        last_pos = {}
        
        for i, char in enumerate(s):
            if char not in first_pos:
                first_pos[char] = i
            last_pos[char] = i
        
        result = []
        
        for char in first_pos:
            if first_pos[char] != last_pos[char]:
                start = first_pos[char] + 1
                end = last_pos[char]
                ascii_sum = sum(ord(s[i]) for i in range(start, end))
                if ascii_sum > 0:
                    result.append(ascii_sum)
        
        return result
