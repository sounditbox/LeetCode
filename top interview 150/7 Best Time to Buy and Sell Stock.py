from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            answer = max(answer, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return answer