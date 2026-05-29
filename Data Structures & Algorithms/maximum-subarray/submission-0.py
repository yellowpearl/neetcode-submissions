class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        current = 0
        for n in nums:
            if current < 0:
                current = 0

            current += n

            max_sum = max(max_sum, current)
        return max_sum