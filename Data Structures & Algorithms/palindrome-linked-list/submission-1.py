# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = prev = ListNode()
        curr = head
        while curr:
            new = ListNode(curr.val)
            new.next = prev
            prev = new
            curr = curr.next
        head2 = prev

        while head:
            print(head2.val, head.val)
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True



        