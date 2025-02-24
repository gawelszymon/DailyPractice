#sprawdzamy od k+1 elementu, wypisujemy ile elementów trzeba zmienic, jesli 
#jesli ilosc elementów które trzeba zmienic jest wiekszy o k 
#wtedy przesuwam moj znacznik na prawo, w innym przypadku przesuwam na prawo
#w zmiennej przechowuje maksymalnie dlugi ciag
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s1n = 0
        d = {}
        l_ele = 0
        for s2n, s2 in enumerate(s):
            if s2 not in d:
                d[s2] = 1
            else:
                d[s2] += 1
            max_ele = max(d.values())
            sum_oth = sum(d.values()) - max_ele
            while sum_oth > k:
                d[s[s1n]] -= 1
                s1n += 1
                max_ele = max(d.values())
                sum_oth = sum(d.values()) - max_ele

            ele = s2n - s1n + 1
            l_ele = max(l_ele, ele)
        return l_ele
