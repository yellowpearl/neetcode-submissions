class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # asddsdf
        res = 0
        chars = set()
        i = 0
        # [] - 0
        # [x] - 1
        # [xa] - 2
        # [xax] - 2
        # [xaxab] - 3
        # [xxxx] - 1
        # [axccxa]
        for j in range(len(s)):
            if s[j] not in chars:
                chars.add(s[j])
            else:
                while s[j] in chars:
                    chars.remove(s[i])
                    i += 1
                chars.add(s[j])
            res = max(res, len(chars))
        return res