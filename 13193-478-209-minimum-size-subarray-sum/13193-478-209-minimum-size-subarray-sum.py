#znalesc ile pierwszych n elementów jest potrzebnych aby spełnic załoezenia
#nastepnie dodac kolejny element i usunąc maksymlanie duzo z poczatku
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        idx = 0
        psa = float("inf")
        for i, num in enumerate(nums):
            s += num
            while s >= target:
                psa = min(psa, i - idx + 1)
                s -= nums[idx]
                idx += 1
            
        return psa if psa != float("inf") else 0