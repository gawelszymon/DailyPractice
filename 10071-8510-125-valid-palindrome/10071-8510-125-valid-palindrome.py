class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        if len(s) == 0:
            return True
        for c in s:
            if s[left] == s[right]:
                if left == right:
                    return True
                if right - left == 1:
                    return True
                left += 1
                right -= 1
                continue
            return False
        