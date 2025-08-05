class Solution:
    def isPalinSent(self, s):
        processed = ''.join(char.lower() for char in s if char.isalnum())
        return processed == processed[::-1]
