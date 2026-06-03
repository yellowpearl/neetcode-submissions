class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        i = 0
        # 1, 2, 3, 4, 4
        for j in range(len(nums)):
            if nums[j] not in unique:
                unique.add(nums[j])
                nums[i] = nums[j]
                i += 1
        
        for j in range(len(nums)-i):
            nums.pop()
        return i