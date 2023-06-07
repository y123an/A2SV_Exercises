# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        
        count = 1
        curr = head

        while curr:
            count +=1
            curr = curr.next

        mid = count/2

        list1 = []
        list2 = []
        curr = head
        while mid > 1:
            list1.append(curr.val)
            curr = curr.next
            mid -= 1
        

        while curr:
            list2.append(curr.val)
            curr = curr.next

        
        for i in range(len(list2)):
            list1[len(list1)-i-1] += list2[i]

        ans = sorted(list1)


        return ans[-1]


        