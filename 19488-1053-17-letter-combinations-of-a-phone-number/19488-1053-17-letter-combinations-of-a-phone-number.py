class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {}
        nums["2"] = "abc"
        nums["3"] = "def"
        nums["4"] = "ghi"
        nums["5"] = "jkl"
        nums["6"] = "mno"
        nums["7"] = "pqrs"
        nums["8"] = "tuv"
        nums["9"] = "wxyz"
        
        sol = []
        def bt(i, cs):
            if len(cs) == len(digits):
                sol.append(cs)
                return
            
            for c in nums[digits[i]]:
                bt(i + 1, cs + c)

        if len(digits) > 0:
            bt(0, "")
        return sol