class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lengh = len(nums)
        if lengh == 0:
            return 0
        
        l = 0
        r = lengh - 1

        # все элементы слева от указателя l - не равны val
        # все элементы справа от указателя r - равны val
        # когда l > r l становится ответом

        # [1, 1, 2], 2
        # [2, 2, 2], 2
        # [1, 1, 1], 2
        # [1], 2 
        # [1], 1
        # [2, 2, 3, 3], 3


        while l <= r:
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l