class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        # [2,10,10,30,30,30]
        for j in range(len(nums)):
            if not j:
                i += 1
            elif nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        
        for j in range(len(nums)-i):
            nums.pop()
        return i
