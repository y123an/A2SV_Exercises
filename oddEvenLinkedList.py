# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
           return head
        f_e = head.next
        even, odd = head.next,head

        while(even and odd):
            odd.next=even.next
            if(odd.next):
                odd=odd.next
            even.next = odd.next
            even = even.next

                

        odd.next=f_e


        return head
        