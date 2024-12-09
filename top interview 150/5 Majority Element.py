from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in set(nums):
            d[num] = nums.count(num)
        return max(d, key=d.get)
