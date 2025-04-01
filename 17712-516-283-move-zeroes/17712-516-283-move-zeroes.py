class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0

        while r < len(nums):
            while r < len(nums) -1 and nums[r] == 0:
                r += 1
            nums[r], nums[l] = nums[l], nums[r]
            r += 1
            l += 1
        return nums
        