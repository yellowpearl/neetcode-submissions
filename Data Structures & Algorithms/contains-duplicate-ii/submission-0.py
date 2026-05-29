class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        
        h = set()
        i = 0
        # 1, 2, 3, 3 k=1
        # 1, k=1
        for j in range(len(nums)):
            if j - i > k:
                h.remove(nums[i])
                i += 1
            
            if nums[j] in h:
                return True
            
            h.add(nums[j])
        return False