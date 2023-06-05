# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        
        count = 1
        curr = head
        while curr.next:
            count += 1
            curr = curr.next
        
        k = k % count

        if k == 0:
            return head
        it = head
        for i in range(count - k -1):
            it = it.next
        
        newHead = it.next
        it.next = None
        curr.next = head
        

        
        return newHead