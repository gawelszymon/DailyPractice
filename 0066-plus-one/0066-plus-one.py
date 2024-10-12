class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(digits)
        
        n = len(digits) - 1
        
        for i in reversed(digits):
            if i != 9:
                i += 1
                digits.pop(n)
                digits.insert(n, i)
                return digits
            elif i == 9 and n == 0:
                digits[n] = 0
                digits.insert(n, 1)
                return digits
            elif i == 9:
                digits[n] = 0
                n -= 1
                continue
                
        