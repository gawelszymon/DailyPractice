# każdą nowa 10 dodaj do hash table z indexem ile razy juz na nią trafilismy
# gdy trafimy na nia i index w hash table wynosi 1 to doaj ją do outputu
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        sol = []
        for i in range(10, len(s) + 1):
            val = s[i - 10: i]
            print(val)
            if val in d and d[val] == 1:
                sol.append(val)
            elif val not in d:
                d[val] = 0
            d[val] += 1
        return sol
