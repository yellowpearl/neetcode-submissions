class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1]
        total = 1
        for n in nums:
            total *= n
            pref.append(total)
        
        post = [1]
        total = 1
        for n in nums[::-1]:
            total *= n
            post.append(total)

        res = []
        for idx, _ in enumerate(nums, start=1):
            res.append(pref[idx-1]*post[len(nums)-idx])
        return res

        # 1 2 4 6

        # 1 1 2  8  48 
        # 1 6 24 48 48

        # idx pref post
        # 1   1-1  len(nums)-idx - 4-1 = 48
        # 2   2-1  len(nums)-idx - 4-2 = 24
        # 3   3-1  len(nums)-idx - 4-3 = 12
        # 4   4-1. 


        # pref=1 2 8 48
        # post=48 48 24 6

        # -1 0 1 2 3
        # -1 0 0 0 0
        #  3 6 6 0 0
        


        