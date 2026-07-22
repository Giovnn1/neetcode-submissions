# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        H = head
        rem = 0
        s = l1.val + l2.val + rem
        H.val = s % 10
        rem = s // 10
        l1, l2 = l1.next, l2.next
        #if l1 is None and l2 is None and rem > 0:
        #    new = ListNode(rem)
        #    H.next = new
        #    return head

        while l1 and l2:
            s = l1.val + l2.val + rem
            rem = s // 10
            new = ListNode(s % 10)
            H.next = new
            H = H.next
            l1, l2 = l1.next, l2.next

        while l1:
            s = l1.val  + rem
            new = ListNode(s % 10)
            rem = s // 10
            H.next = new
            H = H.next
            l1 = l1.next
        while l2:
            s = l2.val  + rem
            new = ListNode(s % 10)
            rem = s // 10
            H.next = new
            H = H.next
            l2 = l2.next

        if rem > 0:
            new = ListNode(rem)
            H.next = new

        return head
