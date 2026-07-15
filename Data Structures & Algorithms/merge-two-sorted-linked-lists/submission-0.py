# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tmp = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val > curr2.val:
                tmp.next = curr2
                tmp = curr2
                curr2 = curr2.next
            else:
                tmp.next = curr1
                tmp = curr1
                curr1 = curr1.next
        if curr1:
            tmp.next = curr1
        else:
            tmp.next = curr2
        return dummy.next