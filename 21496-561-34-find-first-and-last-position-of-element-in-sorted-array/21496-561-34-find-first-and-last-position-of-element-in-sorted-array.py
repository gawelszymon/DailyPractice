class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                mid2 = mid
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                
                while mid2 < len(nums) and nums[mid2] == target:
                    mid2 += 1

                return [mid + 1, mid2 - 1]
            
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]