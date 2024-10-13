class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        if x == 0:
            return 0
        
        if a == 1:
            return 1
        
        while a*a < x:
            a += 1
            
        if(a - 0.000001) * (a - 0.000001) > x:
            a -= 1
        
        return a
        