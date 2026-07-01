class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def comb(remain, stack, start):
            if remain == 0:
                res.append(stack)
            elif remain < 0:
                return
            else:
                for i in range(start, len(nums)):
                    s = stack.copy()
                    s.append(nums[i])
                    comb(remain-nums[i], s, i)
        
        comb(target, [], 0)
        return res

