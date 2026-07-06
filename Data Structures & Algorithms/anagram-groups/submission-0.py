class Solution:
    def getLetters(self, s: str):
        count = [0] * 26
        for letter in s:
            index = ord(letter) - ord('a')
            count[index] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagram = self.getLetters(s)
            anagrams[anagram].append(s)
        return list(anagrams.values())