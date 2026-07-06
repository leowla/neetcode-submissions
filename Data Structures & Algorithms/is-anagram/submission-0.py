class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = {}
        v = {}
        for letter in s:
            u[letter] = u.get(letter, 0) + 1
        for letter in t:
            v[letter] = v.get(letter, 0) + 1
        if u == v:
            return True
        return False