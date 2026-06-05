class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        pref = [0]
        for n in nums:
            total += n
            pref.append(total)

        total = 0
        post = [0]
        for n in nums[::-1]:
            total += n
            post.append(total)


        i = 0
        while pref[i] != post[len(nums)-1-i]:
            i += 1
            if i == len(nums):
                return -1
        return i