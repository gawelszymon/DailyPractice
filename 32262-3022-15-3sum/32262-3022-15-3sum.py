class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        print(nums)
        for idx, num in enumerate(nums):
            if(idx > 0 and num == nums[idx -1]):
                continue
            left = idx + 1
            right = len(nums) - 1
            while(left < right):
                if(num + nums[left] + nums[right] == 0):
                    new_element = [num, nums[left], nums[right]]
                    solution.append(new_element)
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif (num + nums[left] + nums[right]) < 0:
                    left += 1
                elif (num + nums[left] + nums[right]) > 0:
                    right -= 1
        return solution