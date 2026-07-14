import heapq
from collections import defaultdict

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Сформировать мин кучу капитала
        # ?Сформировать макс кучу профитов
        # Попать пока не капитал не превышает w и добавлять в макс кучу профитов по индексу
        # k раз попаем профит, добавляем к w профит, идем по оставшимся капиталам
        capital_dict = defaultdict(list)
        for idx, val in enumerate(capital):
            capital_dict[val].append(idx)

        heapq.heapify(capital)
        profit_h = []

        while capital and capital[0] <= w:
            val = heapq.heappop(capital)
            heapq.heappush_max(profit_h, profits[capital_dict[val].pop()])

        for i in range(k):
            if not profit_h:
                break
            val = heapq.heappop_max(profit_h)
            w += val

            while capital and capital[0] <= w:
                val = heapq.heappop(capital)
                heapq.heappush_max(profit_h, profits[capital_dict[val].pop()])
        return w
