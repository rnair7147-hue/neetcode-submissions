# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diam = 0 

        def height(root):
            nonlocal max_diam
            if root is None:
                return 0

            height_left = height(root.left)
            height_right = height(root.right)

            max_diam = max(max_diam,height_left + height_right)
            
            return 1 + max(height_left, height_right)

        height(root)
        return max_diam
        
        
        