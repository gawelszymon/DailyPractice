class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = (r-l)//2 + l
            if letters[m] > target and letters[m - 1] <= target:
                return letters[m]
            
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return letters[0]
        