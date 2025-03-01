class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        while i < len(nums):
            if nums[i - 2] == nums[i - 1] == nums[i] and len(nums) > 1:
                nums.remove(nums[i])
            else:
                i += 1