# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(root):
    
            if root is None:
                return (True, 0)
        
            left_balanced, left_height = check(root.left)
            right_balanced, right_height = check(root.right)

            height = max(left_height,right_height) + 1

            balanced = (
            left_balanced and
            right_balanced and
            abs(left_height -right_height) <= 1
            )

            return (balanced,height)

        blcd, ht = check(root)
        return blcd