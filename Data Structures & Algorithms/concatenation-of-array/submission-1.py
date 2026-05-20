class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)
        i = 0
        while i < len(nums):
            res[i], res[i+len(nums)] = nums[i], nums[i]
            i += 1
        return res