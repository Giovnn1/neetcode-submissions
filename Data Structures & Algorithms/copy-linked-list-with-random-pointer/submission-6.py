"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head.next is None:
            new = Node(head.val)
            new.next = head.next
            if head.random:
                new.random = new
            return new
       
        new = Node(head.val)
        new_old = {new : head}
        old_new = {head: new}
        
        H = head
        while H.next:
            NEW = Node(H.next.val)
            new_old[NEW] = H.next
            old_new[H.next] = NEW
            old_new[H].next = NEW
            H = H.next
        

        for NEW in new_old:
            OLD = new_old[NEW]
            R = OLD.random
            if R:
                NEW.random = old_new[R]

        return new

