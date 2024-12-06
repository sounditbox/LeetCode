from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.pop()
        i = j = 0
        while j < n:
            while i < len(nums1) and nums1[i] <= nums2[j]:
                i += 1
            nums1.insert(i, nums2[j])
            j += 1
            i += 1


n1 = [4, 5, 6, 0, 0, 0]
s = Solution()
s.merge(n1, 3, [1, 2, 3], 3)
print(n1)
