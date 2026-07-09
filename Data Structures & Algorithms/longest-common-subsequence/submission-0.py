class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1] * len(text1) for i in range(len(text2))]

        # aa ba
        def dfs(t1, t2) -> int:
            if t1 >= len(text1) or t2 >= len(text2):
                return 0
            if cache[t2][t1] != -1:
                return cache[t2][t1]

            if text1[t1] == text2[t2]:
                cache[t2][t1] = 1 + dfs(t1+1, t2+1)
            else:
                cache[t2][t1] = max(dfs(t1+1, t2), dfs(t1, t2+1))
            
            return cache[t2][t1]
        
        return dfs(0, 0)
