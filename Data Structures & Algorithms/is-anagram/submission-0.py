from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counter = defaultdict(int)
        for l in s:
            letter_counter[l] += 1
        for l in t:
            letter_counter[l] -= 1
        return all(l_c == 0 for l_c in letter_counter.values())