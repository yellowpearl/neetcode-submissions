class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # [3,4,5,6,1,2] 
        # 0 5 mid=2
        # 2 5 mid=3
        # 3 5 mid=4
        # 3 4 mid=3
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            else:
                mid = (l+r)//2
                if nums[mid] > nums[l]:
                    l = mid
                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    return min(nums[l], nums[r])
        return min(nums[l], nums[r])