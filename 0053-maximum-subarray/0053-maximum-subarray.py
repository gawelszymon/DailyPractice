class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        arr = []
        maxSub = nums[0]
        for num in nums:
            if sum < 0:
                sum = 0
                arr.clear()
            sum = sum + num
            arr.append(num)
            maxSub = max(maxSub, sum)
        return maxSub