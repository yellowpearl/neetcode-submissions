class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 0
        if counter > max_counter:
            max_counter = counter
        return max_counter
        
        # [1,0,1,0,1,0,1] - 