# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        while head:
            val = head.val
            newNode = ListNode(val)
            temp = reverse
            newNode.next = temp
            reverse = newNode
            head = head.next
        
        return reverse