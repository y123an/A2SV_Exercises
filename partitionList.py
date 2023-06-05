# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        curr = head
        lessx = []
        grex = []

        while curr:
            if curr.val < x:
                lessx.append(curr.val)
            else:
                grex.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        cnode = dummy
        
        for i in range(len(lessx)):
            node = ListNode(lessx[i])
            cnode.next = node
            cnode = node
        
        for i in range(len(grex)):
            node = ListNode(grex[i])
            cnode.next = node
            cnode = node


        return dummy.next

        