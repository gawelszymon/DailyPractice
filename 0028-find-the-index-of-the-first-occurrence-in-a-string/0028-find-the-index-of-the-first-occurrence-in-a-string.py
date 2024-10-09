class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        li = []
        k = 0
        h = 0
        while h < len(haystack):
            if ''.join(li) == needle:
                return k
            if haystack[h] == needle[len(li)]:
                if len(li) == 0:
                    k = h
                li.append(haystack[h])
                h += 1
            elif len(li) > 0 and haystack[h] != needle[len(li)]:
                li.clear()
                h = k + 1
            else:
                h += 1
        if ''.join(li) == needle:
            return k             
        return -1