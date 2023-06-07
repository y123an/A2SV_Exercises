# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodeValues = []
        while head:
            nodeValues.append(head.val)
            head = head.next
        ans = [0] * len(nodeValues)
        stack = []

        for index , val in enumerate(nodeValues):
            while stack and nodeValues[stack[-1]] < val:
                ans[stack.pop()] = val
            stack.append(index) 
        

        return ans



        return ans1
