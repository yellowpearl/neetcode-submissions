class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        # a, bb, ccc
        # 0 1 - 1
        # 1 2 - 3
        # 3 3 - 6

        # a, , ccc
        # 0 1 - 1
        # 1 0 - 1
        # 1 3 - 4

        # a, , 
        # 0 1 - 1
        # 1 0 - 1
        # 1 0 - 1
        # 111$a
        idxs = []
        prev = 0
        for s in strs:
            cur = len(s)
            idxs.append(prev+cur)
            prev += cur
        
        origin_s = "".join(strs)
        idxs_s = ",".join([str(i) for i in idxs])
        return f'{idxs_s}${origin_s}'

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        idxs, origin_s = s.split("$", maxsplit=1)
        res = []
        prev = 0
        # 136$abbccc
        # 136 abbccc
        # 0 1
        # 1 3
        # 3 6

        # 114$accc
        # 0 1
        # 1 1
        # 1 4

        # 111$a
        # 0 1
        # 1 1
        # 1 1
        # 
        for idx in idxs.split(','):
            try:
                i = int(idx)
            except:
                raise ValueError([str(idxs), idx])
            try:
                res.append(origin_s[prev:i])
            except IndexError:
                res.append(origin_s[prev:])
            prev = i
        return res



