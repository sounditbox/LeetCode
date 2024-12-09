from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1
            if count == 3:
                nums.pop(i)
                count -= 1
            else:
                i += 1
        return len(nums)


nums = [1, 1, 1, 2, 2, 3]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)
