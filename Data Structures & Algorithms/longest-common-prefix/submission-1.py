class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = None
        for s in strs:
            if not s:
                return ''
            if prefix is None:
                prefix = s

            startswith = False
            while len(prefix) > 1:
                if s.startswith(prefix):
                    startswith = True
                    break
                else:
                    prefix = prefix[:-1]
            if startswith:
                continue
            elif len(prefix) == 1 and s.startswith(prefix):
                continue
            return ''
        return prefix