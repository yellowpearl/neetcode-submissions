class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        max_i = 0
        max_j = 0
        max_sum = 0

        cur_sum = 0
        i = 0
        # customers = [10,1,7,5], grumpy = [1,0,1,0], minutes = 2
        # 
        for j in range(len(customers)):
            
            cur_sum += customers[j] * grumpy[j]

            if j - i >= minutes:
                cur_sum -= customers[i] * grumpy[i]
                i += 1
            
            if cur_sum >= max_sum:
                max_i = i
                max_j = j
                max_sum = cur_sum
        
        i = max_i
        while i <= max_j:
            grumpy[i] = 0
            i += 1

        res = 0
        for i in range(len(customers)):
            res += customers[i] * int(not bool(grumpy[i]))
        return res

