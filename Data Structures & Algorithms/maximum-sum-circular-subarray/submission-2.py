class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]

        cur_min = 0
        cur_max = 0
        total = 0
        # 5, -3, 5 glob_max=10, glob_min=-3 - 7 - min
        # 1, -3, 1 glob_max=2, glob_min=-3 - 1 - min
        # -3, -1, -1
        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            total += n

            glob_max = max(glob_max, cur_max)
            glob_min = min(glob_min, cur_min)
        
        return max(glob_max, total-glob_min) if glob_max > 0 else glob_max