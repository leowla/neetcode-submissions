class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s for s in s if s.isalnum())
        if s.lower() == s.lower()[::-1]:
            return True
        return False