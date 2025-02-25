#czyli każdy element podciągu ma być powtórzny min k razy, szukam takiego 
#podciagu i zwracam taki najdłuższy podciąg
#czyli sprawdzamy ilość wystapien danych znaków w obrębie jednej iteracji
#targqt unique
#w momencie kiedy wszystko bedzie git tzn ilosc elementów bedzie <= od
#target unique przesowamy prawa czesc okna, jesli nie jest git,
#przesuwamy lewą część okna i usuwamy przesunięty element 
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        l_count = Counter(s)
        final = 0
        for lc in range(1, len(l_count) + 1):
            ls = {}
            lp = 0
            rp = 0
            while rp < len(s):
                char = s[rp]
                if char not in ls:
                    ls[char] = 1
                else:
                    ls[char] += 1
                rp += 1

                while len(ls) > lc:
                    ls[s[lp]] -= 1
                    if ls[s[lp]] == 0:
                        del ls[s[lp]]
                    lp += 1

                if len(ls) == lc and all(value >= k for value in ls.values()):
                    current_length = rp - lp
                    final = max(final, current_length)

            
        return final