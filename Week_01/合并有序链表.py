# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1 
        node1,node2,flag= l1,l2,ListNode(0)
        result = flag
        while node1 is not None and node2 is not None:
            if node2.val <= node1.val:
                flag.next = node2
                flag = flag.next
                node2 = node2.next
            else:
                flag.next  = node1
                flag = flag.next
                node1 = node1.next
        if node1 is not None:
            flag.next = node1
        if node2 is not None:
            flag.next = node2
        return result.next
        # while node1 is not None and node2 is not None:
        #     if node2.val <= node1.val:
        #         node1.next = node2
        #         node2 = node2.next
        #         flag = node2
        #     else:
        #         node1 = node1.next
        #         flag = node1
            
        # # if node1:
        # #     flag.next = node1
        # # if node2:
        # #     flag.next = node2
        # return l1

            