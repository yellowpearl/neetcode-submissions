class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h = {}
        restricted = set()
        for i in range(len(s)):
            if s[i] not in h:
                if t[i] in restricted:
                    return False
                h[s[i]] = t[i]
                restricted.add(t[i])
            elif h[s[i]] != t[i]:
                return False
        return True