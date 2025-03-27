class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for a in matrix:
            if a[-1] < target:
                continue
            l = 0
            r = len(a) - 1
            while l <= r:
                m = (r -l) // 2 + l
                if a[m] == target:
                    return True
                
                if a[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False
        