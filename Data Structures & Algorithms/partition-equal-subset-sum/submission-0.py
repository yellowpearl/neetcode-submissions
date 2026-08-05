class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 > 0:
            return False
        t = s // 2

        mem1 = [0] * (t+1)
        mem2 = [0] * (t+1)

        for i in range(1, len(nums)+1):
            n = nums[i-1]
            for j in range(t+1):
                skip = mem1[j]

                include = 0
                if n <= j:
                    include = n + mem1[j-n]
                mem2[j] = max(skip, include)
            mem1 = mem2
            mem2 = [0] * (t+1)
        return mem1[t] == t

        