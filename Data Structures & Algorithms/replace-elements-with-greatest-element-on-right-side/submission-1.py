class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        i = len(arr) - 1
        m = arr[-1]
        while i > 0:
            copy = arr[i]
            arr[i] = m
            m = max(m, copy)
            i -= 1
        arr[i] = m
        arr[-1] = -1
        return arr
