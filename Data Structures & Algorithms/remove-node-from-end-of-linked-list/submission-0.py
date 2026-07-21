# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        H = head
        l = 0
        while H:
            H = H.next
            l += 1

        if n == l:
            H = head.next
            head.next = None
            return H

        H = head
        for _ in range(l - n - 1):
            H = H.next
        S = H.next
        C = H.next.next
        H.next = C
        S.next = None
        return head
