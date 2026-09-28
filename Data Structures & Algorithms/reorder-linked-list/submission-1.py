# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:

#         # find the middle
#         # Reverse the second half
#         # connect the pointers

#         if head is None or head.next is None:
#             return

#         # Finding the middle        
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         second_half = slow.next
#         slow.next = None

#         #Reverse the second_half

#         prev = None
#         curr = second_half

#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
        
#         # connect the 0 - n-1 , 1- n-2 

#         first = head
#         second = prev

#         while second:
#             temp1 = first.next
#             temp2 = second.next
#             first.next = second
#             second.next = temp1
#             first = temp1
#             second = temp2
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast =  head , head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first , second = head , prev

        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

























        

