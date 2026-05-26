class ListNode:
    def __init__(
        self,
        val: int, 
        prev: ListNode | None = None, 
        next: ListNode | None = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        if not cur:
            return -1
        while index > 0:
            cur = cur.next
            index -= 1
            if not cur:
                return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, next=self.head)
        if self.head:
            self.head.prev = new_head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val, prev=self.tail)
        if self.tail:
            self.tail.next = new_tail
            self.tail = new_tail
        else:
            self.head = new_tail 
            self.tail = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        # 1, 2
        if not self.head and not self.tail:
            new_node = ListNode(val)
            self.head = new_node
            self.tail = new_node
            return

        cur = self.head # 1
        prev = None # None
        i = index # 0

        # 1, 2 i=3
        while i > 0:
            i -= 1
            prev = cur
            if not prev and not cur:
                return
            cur = cur.next
        

        new_node = ListNode(val, prev=prev, next=cur) # 1 None 2



        if prev:
            prev.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        if new_node.next is None:
            self.tail = new_node
        if new_node.prev is None:
            self.head = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        prev = None
        i = index
        while i > 0:
            prev = cur
            cur = cur.next
            i -= 1

            if not cur:
                return
        
        if cur.next:
            cur.next.prev = prev
        if prev:
            prev.next = cur.next
        if cur is self.head:
            self.head = cur.next
        if cur is self.tail:
            self.tail = cur.prev
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)