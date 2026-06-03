class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = None
        i = 0
        cur_sum = 0
        # 1, 2, 1 | 5 - 4
        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                if res:
                    res = min(res, j-i+1)
                else:
                    res = j-i+1
                cur_sum -= nums[i]
                i += 1
        return res if res else 0
                    