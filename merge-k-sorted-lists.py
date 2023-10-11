# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = ListNode()
        def sortList(list1, list2):
            newNode = dummy = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    newNode.next = list2
                    newNode = newNode.next
                    list2 = list2.next
                else:
                    newNode.next = list1
                    newNode = newNode.next
                    list1 = list1.next

            while list1:
                newNode.next = list1
                list1 = list1.next
                newNode = newNode.next
            while list2:
                newNode.next = list2
                list2 = list2.next
                newNode = newNode.next
            newNode.next = None

            return dummy.next

        sortedList = sortedList.next
        for x in lists:
            sortedList = sortList(sortedList,x)
        
        return sortedList