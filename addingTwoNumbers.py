# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        total = int(num1_rev) + int(num2_rev)

        ans = str(total)
        head = None
        prev = None
        for i in range(len(ans)):
            head = ListNode(ans[i],prev)
            prev = head
            
        return head