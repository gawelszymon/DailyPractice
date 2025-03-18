class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        i = 0
        j = len(nums) - 1
        q = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                q += 1
                k = i
                i += 1
                while i < j and nums[i] + nums[j] < target:
                    q += 1
                    i += 1
                i += 1
                i = k
                j -= 1
        return q
            