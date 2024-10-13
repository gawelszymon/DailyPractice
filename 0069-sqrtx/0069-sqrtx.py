class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        s = 1
        e = x
        while s <= e:
            m = (s + e) // 2  # Integer division
            
            # Check if the square of m equals x
            if m * m == x:
                return m
            # If the square of m is greater than x, move the upper bound
            elif m * m > x:
                e = m - 1
            # If the square of m is less than x, move the lower bound
            else:
                s = m + 1
        
        # Return the closest integer less than the square root
        return e