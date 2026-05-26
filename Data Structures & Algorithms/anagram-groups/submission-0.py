from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: list[tuple[dict, list[str]]] = []
        for s in strs:
            s_d = defaultdict(int)
            for letter in s:
                s_d[letter] += 1
            
            added = False
            for res_dict, res_list_elem in res:
                if s_d == res_dict:
                    res_list_elem.append(s)
                    added = True
                    break
            if not added:
                res.append((s_d, [s]))
            
        return [res_list for _, res_list in res]
