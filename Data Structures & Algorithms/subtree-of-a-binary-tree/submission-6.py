# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            if p.val != q.val:
                return False
        
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)

            return left and right

        # if root is None and subRoot is None:
        #     return True
        # if root is None and subRoot is not None:
        #     return False
        # if root is not None and subRoot is None:
        #     return True
        # if root.val != subRoot.val:
        #     if root.left is not None:
        #         root = root.left  
        #         return self.isSubtree(root, subRoot)              
        #     elif root.right is not None:
        #         root = root.right 
        #         return self.isSubtree(root, subRoot)               
        #     else:
        #         return False
        # else:
        #     return sameTree(root, subRoot)
        # subRoot is empty
        if subRoot is None:
            return True

        # root is empty, but subRoot isn't
        if root is None:
            return False

        # Try matching subRoot starting at this node
        if sameTree(root, subRoot):
            return True

        # If it didn't match, search BOTH sides
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

        

            

         