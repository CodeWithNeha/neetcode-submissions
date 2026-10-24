# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftSub = self.maxDepth(root.left)
        rightSub = self.maxDepth(root.right)
        diameter = leftSub+rightSub
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(sub, diameter)
        