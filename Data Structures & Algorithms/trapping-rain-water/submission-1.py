class Solution:
    def trap(self, height: List[int]) -> int:
        h = height

        res = 0
        tmp_res = 0

        l = 0
        # [0,2,0,3,1,0,1,3,2,1] l=0 r=0 tmp=0 res=0
        # [0,2,0,3,1,0,1,3,2,1] l=0 r=1 tmp=0 res=0
        # [0,2,0,3,1,0,1,3,2,1] l=1 r=2 tmp=0 res=0
        # [0,2,0,3,1,0,1,3,2,1] l=1 r=3 tmp=2 res=0
        # [0,2,0,3,1,0,1,3,2,1] l=3 r=4 tmp=0 res=2
        # [0,2,0,3,1,0,1,3,2,1] l=3 r=5 tmp=2 res=2
        # [0,2,0,3,1,0,1,3,2,1] l=3 r=6 tmp=5 res=2
        # [0,2,0,3,1,0,1,3,2,1] l=3 r=7 tmp=7 res=2
        # [0,2,0,3,1,0,1,3,2,1] l=7 r=8 tmp=1 res=9
        # [0,2,0,3,1,0,1,3,2,1] l=7 r=9 tmp=3 res=9
        
        for r in range(len(h)):
            if r:
                if h[r] >= h[l]:
                    l = r
                    res += tmp_res
                    tmp_res = 0
                else:
                    tmp_res += h[l] - h[r]
        tmp_res = 0
        h = h[::-1]
        m = l
        l = 0
        for r in range(len(h)):
            if r and r < len(h) - m:
                if h[r] >= h[l]:
                    l = r
                    res += tmp_res
                    tmp_res = 0
                else:
                    tmp_res += h[l] - h[r]
        return res

