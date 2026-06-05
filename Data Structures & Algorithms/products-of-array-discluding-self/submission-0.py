class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for n in nums:
            if n != 0:
                total *= n
            else:
                zero_count += 1


        if zero_count == 0:
            return [int(total/n) for n in nums]
        elif zero_count == 1:
            return [0 if n != 0 else total for n in nums]
        else:
            return [0 for n in nums]
        