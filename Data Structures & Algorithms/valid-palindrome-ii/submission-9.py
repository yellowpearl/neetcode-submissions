class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_poly(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False, l, r
                l += 1
                r -= 1
            return True, None, None

        l, r = 0, len(s) - 1
        is_p, l, r = is_poly(l,r)
        if not is_p:
            return is_poly(l+1, r)[0] or is_poly(l, r-1)[0]
        else:
            return True
