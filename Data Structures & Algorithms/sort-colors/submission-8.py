class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2, 0, 2, 1, 1, 0] -> [0, 0, 1, 1, 2, 2]
        # 2 2 2
        # 0 2 4
        bucket = [0, 0, 0]
        for n in nums:
            bucket[n] += 1
        
        for i in range(len(nums)):
            if bucket[0] > 0:
                nums[i] = 0
                bucket[0] -= 1
            elif bucket[1] > 0:
                nums[i] = 1
                bucket[1] -= 1
            elif bucket[2] > 0:
                nums[i] = 2
                bucket[2] -= 1
            
            