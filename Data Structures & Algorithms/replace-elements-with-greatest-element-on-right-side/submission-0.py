class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lengh = len(arr)
        l = 0
        while l < lengh - 1:
            arr[l] = max(arr[l + 1:])
            l += 1
        arr[lengh-1] = -1
        return arr