class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        p_count = Counter(p)
        s_count = Counter(s[:m])
        val = []

        if s_count == p_count:
            val.append(0)

        for i in range(m, n):
            s_count[s[i]] += 1
            s_count[s[i - m]] -= 1

            if s_count == p_count:
                val.append(i - m + 1)

        return val  