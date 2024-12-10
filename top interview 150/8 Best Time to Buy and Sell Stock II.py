from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_inds = []
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            min_inds.append(i)
            i += 1
        if min_inds and min_inds[-1] == len(prices) - 1:
            min_inds.pop()
        if not min_inds:
            return 0
        for ind in min_inds:
            next_max = ind + 1
            while next_max < len(prices) and prices[ind] >= prices[next_max]:
                next_max += 1
            answer += prices[next_max] - prices[ind]
        return answer


s = Solution()
print(s.maxProfit([1]))
