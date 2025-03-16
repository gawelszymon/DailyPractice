class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def longest_recursive(i, pv):
    #         if(not nums or i == len(nums)):
    #             return 0

    #         skip = longest_recursive(i + 1, pv)

    #         take = 0
    #         if(pv == -1 or nums[i] > nums[pv]):
    #             take = 1 + longest_recursive(i + 1, i)
    #         return max(skip, take)
        
    #     return longest_recursive(0, -1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            l = 0
            h = len(sub) - 1
            while l <= h:
                m = (h - l) // 2 + l
                if num <= sub[m]:
                    if m > 0 and (sub[m - 1] < num):
                        sub[m] = num
                        break
                    elif m == 0:
                        sub[m] = num
                        break
                    else:
                        h = m
                else:
                    l = m + 1
            if l > h:    
                sub.append(num)
        return len(sub)