#so first of all I have to sort it and then I compare a result to previous one
#if the difference is bigger than the previous one I return the previous sum
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum1 = float('inf')
        for n in range(len(nums) - 2):
            l = n + 1
            r = len(nums) - 1
            while l < r:
                sum2 = nums[n] + nums[l] + nums[r]
                if abs(sum2 - target) < sum1:
                    sa = nums[n] + nums[l] + nums[r]
                    sum1 = abs(sum2 - target)
                if sum2 < target:
                    l += 1
                elif sum2 > target:
                    r -= 1
                else:
                    return sum2
        return sa
