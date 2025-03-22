class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        r = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1
        
        if idx < len(s) and s[idx] == "-":
            v = -1
            idx += 1
        elif idx < len(s) and s[idx] == "+":
            v = 1
            idx += 1
        else:
            v = 1

        while idx < len(s) and '0' <= s[idx] <= '9':
            r = 10*r + (ord(s[idx]) - ord('0'))

            if r > (2**31 - 1):
                return 2**31 - 1 if v == 1 else -2**31
            idx += 1
        return v*r   
        