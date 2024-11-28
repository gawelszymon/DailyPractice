class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        pl = 0
        for i in range(len(s)):
            r, l = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > pl:
                    p = s[l:r+1]
                    pl = len(p)
                r += 1
                l -= 1
            r = i + 1
            l = i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if r - l + 1 > pl:
                    p = s[l:r+1]
                    pl = len(p)
                r += 1
                l -= 1   
        return p
                
            