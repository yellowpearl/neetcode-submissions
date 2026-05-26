class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        prev = None
        # 
        for n in sorted_nums:
            if n == prev:
                return True
            prev = n
        return False