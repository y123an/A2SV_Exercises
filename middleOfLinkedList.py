# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        count = 1

        while curr:
            curr = curr.next
            count += 1
             
        midNode = head

        mid = count / 2
        while mid > 1:
            midNode = midNode.next
            mid -=1
    
      

        return midNode
        