class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr, res = [], []
        # [112] [11] [1] [2]
        def back(i, curr, res):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            back(i+1, curr, res)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            back(i+1, curr, res)
        back(0, curr, res)
        return res