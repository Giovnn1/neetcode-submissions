# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        A, B = head.next, head.next.next
        while B:
            if B.next is None:
                return False
            if A == B :
                return True
            A = A.next
            B = B.next.next
        return False