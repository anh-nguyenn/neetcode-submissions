# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of linked list
        curr = head
        lengL = 0
        while curr:
            lengL += 1
            curr = curr.next
        removeIdx = lengL - n
        if not head.next and removeIdx == 0:
            return
        dummy = start = ListNode()
        start.next = head
        i = 0
        while i < removeIdx and start:
            i += 1
            start = start.next 
        if start and start.next:
            if start.next == None:
                start.tail == start
            start.next = start.next.next
        return dummy.next
        

