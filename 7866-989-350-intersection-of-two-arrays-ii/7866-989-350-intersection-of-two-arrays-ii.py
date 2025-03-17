from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        count = Counter(nums1)
        s = []
        for n1 in nums1:
            l = 0
            h = len(nums2) - 1
            while l <= h:
                m = (h - l) // 2 + l
                if nums2[m] == n1 and count[n1] > 0:
                    s.append(n1)
                    count[n1] -= 1
                    nums2.pop(m)
                    break
                elif nums2[m] < n1:
                    l = m + 1
                else:
                    h = m - 1
        return s