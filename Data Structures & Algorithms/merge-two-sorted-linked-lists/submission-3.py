# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1 and list2 is None:
        #     return None
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1

        # head1 = list1
        # final = []

        # while head1:
        #     final.append(head1.val)
        #     head1 = head1.next
        
        # head2 = list2

        # while head2:
        #     final.append(head2.val)
        #     head2 = head2.next

        # final.sort()

        # # 1. Create the head node with the first element
        # head = ListNode(final[0])
        # current = head

        # # 2. Loop through the remaining elements and link them
        # for item in final[1:]:
        #     current.next = ListNode(item)
        #     current = current.next

        # return head

        dummy = node = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next
        node.next = list1 or list2

        return dummy.next

        



        