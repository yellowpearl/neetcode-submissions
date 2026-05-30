class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i = 0
        j = 0
        window_sum = 0
        # arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        for j in range(len(arr)):
            window_sum += arr[j]
            if j - i >= k:
                window_sum -= arr[i]
                i += 1
            if j - i == k - 1 and window_sum / k >= threshold:
                res += 1
        return res

