class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        size = 0
        while right != left:
            tem_size = min(height[left], height[right]) * (right -left)
            size = max(size, tem_size)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return size