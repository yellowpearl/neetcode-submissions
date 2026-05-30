class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = None
        for letter in s:
            if not prev:
                prev = letter
            else:
                res += abs(ord(letter)-ord(prev))
                prev = letter
        return res