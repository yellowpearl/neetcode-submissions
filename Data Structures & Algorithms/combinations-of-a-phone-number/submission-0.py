class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def back(i, curr, res):
            if i == len(digits):
                res.append(''.join(curr))
                return


            for l in d[digits[i]]:
                curr.append(l)
                back(i+1, curr, res)
                curr.pop()
        
        res = []
        back(0, [], res)
        return res
