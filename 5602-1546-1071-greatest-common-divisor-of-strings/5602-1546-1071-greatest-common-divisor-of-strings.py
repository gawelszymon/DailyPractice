class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def div(s, t):
            if len(t) % len(s) != 0:
                return False
            m = len(t) // len(s)
            return m * s == t
        
        for l in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % l == 0 and len(str2) % l == 0:
                sub = str1[:l]
                if div(sub, str1) and div(sub, str2):
                    return sub
        
        return ""