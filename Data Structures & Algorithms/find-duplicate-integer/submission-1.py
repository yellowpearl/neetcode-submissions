class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = nums[0], nums[0]
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        # 3,1,3,4,2
        # 3 3
        # 4 2
        # 4 3
        # 3 2
        # 4 4
        s2 = nums[0]
        while s2 != s:
            s = nums[s]
            s2 = nums[s2]
        return s
