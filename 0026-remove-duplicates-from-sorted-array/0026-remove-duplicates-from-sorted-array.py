class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        q = 0
        for i in range (len(nums)):
            if nums[i] != nums[q]:
                q += 1
                nums[q] = nums[i]
        return q + 1
    