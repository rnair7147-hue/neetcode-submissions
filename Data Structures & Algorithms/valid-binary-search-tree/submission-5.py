# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, low , high):

            if root is None:
                return True

            if not (low < root.val < high):
                return False
            
            left_tree_valid = validate(root.left,low,root.val)
            right_tree_valid = validate(root.right, root.val, high)

            return left_tree_valid and right_tree_valid

        return validate(root, float('-inf'), float('inf'))


        
        
            
