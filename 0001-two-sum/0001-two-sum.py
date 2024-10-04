class Solution(object):
    def twoSum(self, nums, target):
        for l in range(len(nums)):
            for j in range(len(nums)):
                if l == j:
                    continue
                elif nums[l] + nums[j] == target:
                    solution = [l, j]
                    return solution
                else:
                    continue