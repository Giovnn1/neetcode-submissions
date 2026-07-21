# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        #find mid-point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        #reverse second half
        if mid.next.next:
            A, B = mid.next, mid.next.next
            A.next = None
            while B:
                C = B.next
                B.next = A
                A, B = B, C 
            #A is now the head of the reversed list
        else:
            #this is the case in which the list has length = 3
            A = mid.next
            A.next = None
        mid.next = None

        #zip the lists
        H = head
        while A:
            NH = H.next
            NA = A.next
            H.next = A
            A.next = NH
            H, A = NH, NA

        return 










            