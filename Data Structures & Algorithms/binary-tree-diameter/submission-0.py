# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
       
            left_tree = dfs(node.left)
            right_tree = dfs(node.right) 

            self.max_diameter = max(self.max_diameter,left_tree + right_tree)
            return max(left_tree, right_tree) + 1
        dfs(root)
        return self.max_diameter