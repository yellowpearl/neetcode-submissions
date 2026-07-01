from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            sub_res = [item for item in res]
            for r in sub_res:
                c = [item for item in r]
                c.append(n)
                res.append(c)
        return res