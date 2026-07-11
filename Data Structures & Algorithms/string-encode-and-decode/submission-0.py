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
            msg_length = int(s[i:delimiter_index])
            end = (delimiter_index + 1) + msg_length
            decoded.append(s[delimiter_index+1:end])
            i = end
        return decoded