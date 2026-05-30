class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        toggle = True
        # "   fly moon  " - 4
        # "luffy joyboy"
        for letter in s:
            if letter != ' ':
                if toggle:
                    res = 1
                else:
                    res += 1
                toggle = False
            else:
                toggle = True
        return res