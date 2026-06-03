class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if j < 2:
                i += 1
            elif (
                nums[j] != nums[i-1]
             ) or (
                nums[j] == nums[i-1] and nums[i-1] != nums[i-2]
            ):
                nums[i] = nums[j]
                i += 1
        return i