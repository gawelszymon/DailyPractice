class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x        
        s = 1
        e = x
        while s <= e:
            m = (s + e) // 2            
            if m * m == x:
                return m
            elif m * m > x:
                e = m - 1
            else:
                s = m + 1       
        return e