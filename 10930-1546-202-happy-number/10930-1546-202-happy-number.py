class Solution:
    def isHappy(self, n: int) -> bool:
        l = []

        while n not in l:
            l.append(n)
            n = self.happy(n)
            if n == 1:
                return True
        return False

    def happy(self, n):
        sum = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            sum += digit
            n = n // 10
        return sum

        
        