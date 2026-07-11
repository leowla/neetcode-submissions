class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "|" + s
        return encoded
        # e.g. encoded = 5|Hello5|World

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delimiter_index = s.find('|', i)
            length = int(s[i:delimiter_index])
            content_start = delimiter_index + 1
            content_end = content_start + length
            decoded.append(s[content_start:content_end])
            i = content_end
        return decoded