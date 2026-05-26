from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: dict[tuple[str, int], list[str]] = defaultdict(list)
        for s in strs:
            s_d = defaultdict(int)
            for letter in s:
                s_d[letter] += 1
            res[tuple(sorted(s_d.items()))].append(s)     
        return list(res.values())
