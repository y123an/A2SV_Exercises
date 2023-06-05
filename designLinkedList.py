class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left 
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index>0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        curr = self.left.next
        node.next = curr
        curr.prev = node
        self.left.next =node
        node.prev = self.left
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        curr = self.right.prev
        node.next = self.right
        curr.next = node
        node.prev = curr
        self.right.prev = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next 
        while curr and index >0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node = ListNode(val)
            next = curr
            prev = curr.prev
            node.next = next
            next.prev = node
            node.prev = prev
            prev.next = node
            

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next 
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            next,prev = curr.next ,curr.prev
            next.prev = prev
            prev.next = next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)