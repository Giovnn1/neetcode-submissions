# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        H = head
        carry = 0
        s = l1.val + l2.val + carry
        H.val = s % 10
        carry = s // 10
        l1, l2 = l1.next, l2.next
        

        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            new = ListNode(s % 10)
            H.next = new
            H = H.next
            l1, l2 = l1.next, l2.next

        while l1:
            s = l1.val  + carry
            new = ListNode(s % 10)
            carry = s // 10
            H.next = new
            H = H.next
            l1 = l1.next
        while l2:
            s = l2.val  + carry
            new = ListNode(s % 10)
            carry = s // 10
            H.next = new
            H = H.next
            l2 = l2.next

        if carry > 0:
            new = ListNode(carry)
            H.next = new

        return head
