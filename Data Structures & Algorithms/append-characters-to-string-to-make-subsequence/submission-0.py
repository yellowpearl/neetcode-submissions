class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = 0
        i = 0
        # a a - 0
        # a b - 1
        # aga agtt - 
        for j in range(len(s)):
            if s[j] == t[i]:
                i += 1
                if i == len(t):
                    break
        while i < len(t):
            res += 1
            i += 1
        return res