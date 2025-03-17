class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        s = set()
        for n1 in nums1:
            l = 0
            r = len(nums2) - 1
            while l <= r:
                m = (r - l) // 2 + l
                if nums2[m] == n1:
                    s.add(n1)
                    break
                elif nums2[m] < n1:
                    l = m + 1
                else:
                    r = m - 1
        return list(s)