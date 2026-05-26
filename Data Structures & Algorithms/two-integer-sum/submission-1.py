class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = 0
        f = 1
        while s < len(nums):
            while f < len(nums):
                if nums[s] + nums[f] == target:
                    return [s, f]
                f += 1
            s += 1
            f = s + 1
