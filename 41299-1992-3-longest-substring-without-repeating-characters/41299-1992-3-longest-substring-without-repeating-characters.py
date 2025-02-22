class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mdict = {}
        l = 0
        maxlens = 0
        for i, char in enumerate(s):
            if s[i] in mdict and mdict[char] >= l:
                l = mdict[char] + 1
            mdict[char] = i
            maxlens = max(maxlens, i - l + 1)
        return maxlens