class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = None
        for i in range(len(arrays)):
            if i:
                cur_min = arrays[i][0]
                cur_max = arrays[i][-1]

                cur_min_dis = abs(glob_max - cur_min)
                cur_max_dis = abs(cur_max - glob_min)

                if res is None:
                    res = max(cur_min_dis, cur_max_dis)
                else:
                    res = max(cur_min_dis, cur_max_dis, res)

                glob_min = min(glob_min, cur_min)
                glob_max = max(glob_max, cur_max)
            else:
                glob_min = arrays[i][0]
                glob_max = arrays[i][-1]

        return res

        
        


