class Solution:
    def rob(self, nums: List[int]) -> int:
        # 5 1 9 1 1 9 1 5
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]
            else:
                cache[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            
            return cache[i]
        
        return dfs(0)