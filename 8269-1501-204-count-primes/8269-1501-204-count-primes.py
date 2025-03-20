class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        pri = [True] * n
        pri[0] = pri[1] = False
        for i in range(2, int(n**0.5) + 1):
            if pri[i]:
                for j in range(i*i, n, i):
                    pri[j] = False
        # k = 0
        # for i in range(len(pri)):
        #     if pri[i] == True:
        #         k += 1
        return sum(pri)