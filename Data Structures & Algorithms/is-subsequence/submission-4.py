class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        cur = 0
        # s=axc t=bahegdx
        res = False
        for letter in t:
            if letter == s[cur]:
                cur += 1
                if cur > len(s) - 1:
                    res = True
                    break
        return res