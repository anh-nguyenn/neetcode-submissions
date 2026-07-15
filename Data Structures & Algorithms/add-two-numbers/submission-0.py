class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLL(l):
            prev = None
            curr = l
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        def llToInt(l):
            total = 0
            while l:
                total = total * 10 + l.val
                l = l.next
            return total
        def intToLL(num):
            s = str(num)
            dummy = curr = ListNode(0)
            for char in s:
                curr.next = ListNode(int(char))
                curr = curr.next
            return dummy.next
        re1 = reverseLL(l1)
        re2 = reverseLL(l2)

        total = llToInt(re1) + llToInt(re2)

        res = intToLL(total)

        return reverseLL(res)