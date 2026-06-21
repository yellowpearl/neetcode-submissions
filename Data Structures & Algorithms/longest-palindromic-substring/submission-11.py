class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 1
        res = 0
        for i in range(len(s)):
            if i and i <= len(s)-2 and s[i-1] == s[i+1]:
                l = i-1
                r = i+1
                while s[l] == s[r]:
                    if r-l+1 > res_len:
                        res_len = r-l+1
                        res = l
                    l -= 1
                    r += 1
                    if l < 0 or r > len(s)-1:
                        break
            if i <= len(s)-2 and s[i] == s[i+1]:
                l = i
                r = i+1
                while s[l] == s[r]:
                    if r-l+1 > res_len:
                        res_len = r-l+1
                        res = l
                    l -= 1
                    r += 1
                    if l < 0 or r > len(s)-1:
                        break
            
            
        return s[res:res+res_len]
        