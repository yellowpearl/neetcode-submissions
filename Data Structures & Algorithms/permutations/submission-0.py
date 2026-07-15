class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for n in nums:
            n_perm = []
            for p in perm:
                for i in range(len(p)+1):
                    p_c = p.copy()
                    p_c.insert(i, n)
                    n_perm.append(p_c)
            perm = n_perm
        return perm
            