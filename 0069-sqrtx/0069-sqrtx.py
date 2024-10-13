class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        s = 1
        e = x
        m = (e-s)/2 + s
        mt = []
        mt.append(m)
        mtl = []
        mtu = []
        
        
        while (len(mtu) < 1 or len(mtl) < 1 or len(mt) < 50) or ((floor(mt[-1]) != floor(mt[-2]) or (mt[-1] != mtu[-1] or mt[-2] != mtl[-1])) and (floor(mt[-1]) != floor(mt[-2]) or (mt[-1] != mtl[-1] or mt[-2] != mtu[-1]))) :        
            if mt[-1] * mt[-1] > x:
                e = m
                m = (e-s)/2 + s
                mtl.append(m)
                mt.append(m)
            elif mt[-1] * mt[-1] < x:
                s = m
                m = (e-s)/2 + s
                mtu.append(m)
                mt.append(m)
            elif mt[-1] * mt[-1] == x:
                return floor(mt[-1])

        
        return floor(mtl[-1])

        