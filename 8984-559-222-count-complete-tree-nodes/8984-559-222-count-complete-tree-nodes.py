# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        n1 = [1]
        def count(node, n):
            if not node:
                return
            if node.right:
                n[0] += 1
                count(node.right, n)
            if node.left:
                n[0] += 1
                count(node.left, n)

        if not root:
            return 0
        
        count(root, n1)
        return n1[0]