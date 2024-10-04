class Solution(object):
    def twoSum(self, nums, target):
        for k in range(len(nums)):
            for j in range(len(nums)):
                if k == j:
                    continue
                elif nums[k] + nums[j] == target:
                    solution = [k, j]
                    return solution
                else:
                    continue