# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        dummy = ListNode(0,head)
        curr = dummy
        prev = head
        aft = head.next

        while aft:
            if prev.val == aft.val:
                if not aft.next:
                    curr.next = aft.next 
                    prev = aft.next
                    aft = None
                    continue

                while prev.val == aft.val:
                    aft = aft.next
                    if not aft:
                        curr.next = None
                        break
                prev = aft
                curr.next = aft
                if aft:
                    aft = aft.next
            else:
                prev = prev.next
                curr = curr.next
                aft = aft.next

        
        return dummy.next