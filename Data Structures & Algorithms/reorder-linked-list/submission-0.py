# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return
        
        # 1. Store node references in an array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # 2. Use two pointers to re-link nodes in-place
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            # Point left node to right node
            nodes[left].next = nodes[right]
            left += 1
            
            # Check if pointers met in the middle (odd length edge case)
            if left >= right:
                break
            
            # Point right node to the next left node
            nodes[right].next = nodes[left]
            right -= 1
        
        # 3. CRITICAL: Break the cycle at the end node
        nodes[left].next = None

        head = nodes


        