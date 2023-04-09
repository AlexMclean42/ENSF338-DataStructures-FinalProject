from DNode import DNode
from doublyLL import DoublyLL

class doublyCLL(DoublyLL):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.size == 0
    
    def InsertHead(self, node):
        if not self.head:
            node.prev = node
            node.next = node
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.size += 1
    
    def InsertTail(self, node):
        if not self.tail:
            self.InsertHead(node)
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def Insert(self, node, position):
        if position == 0:
            self.InsertHead(node)
        elif position >= self.size:
            self.InsertTail(node)
        else:
            current = self.head
            for i in range(1, position):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1
    
    def SortedInsert(self, node):
        if not self.head:
            self.InsertHead(node)
        elif node.data <= self.head.data:
            self.InsertHead(node)
        elif node.data >= self.tail.data:
            self.InsertTail(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1
    
    def is_sorted(self):
        if not self.tail:
            return True
        current = self.tail.next
        while current != self.tail:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    
    def length(self):
        return self.size

    def Search(self, node):
        current = self.head
        while current and current != self.tail:
            if current.data == node.data:
                return current
            current = current.next
        if current == self.tail and current.data == node.data:
            return current
        return None
    
    def DeleteHead(self):
        if not self.head:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
        temp.next = None
        temp.prev = None
        self.size -= 1
        return temp
    
    def DeleteTail(self):
        if not self.tail:
            return None
        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        temp.next = None
        temp.prev = None
        self.size -= 1
        return temp
    
    def Delete(self, node):
        if not self.head:
            return
        current = self.head
        position = 0
        while current:
            if current == node:
                break
            current = current.next
            position += 1
            if current == self.head:
                return
        if position == 0:
            self.DeleteHead()
        elif position == self.size - 1:
            self.DeleteTail()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None
            self.size -= 1
    
    def Print(self):
        if self.is_empty():
            print("The list is empty.")
            return
        print("List length:", self.length())
        print("Sorted:", "Yes" if self.is_sorted() else "No")
        print("List content:", end=" ")
        current = self.head
        for i in range(self.size):
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    # Create nodes
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)

    # Create circular linked list
    clist = doublyCLL()
    print("Creating new circular linked list:")
    clist.Print()
    clist.Insert(node1, 0)
    clist.Insert(node2, 1)
    clist.Insert(node3, 2)

    # Print circular linked list
    print("\nPrinting initial circular linked list:")
    clist.Print()

    # Demonstrate search functionality
    print("\nSearching for node with data value 2:")
    result = clist.Search(DNode(2))
    if result:
        print("Node found with data value 2")
    else:
        print("Node not found with data value 2")

    # Demonstrate SortedInsert functionality
    print("\nInserting new node with data value 2.5 in sorted order:")
    clist.SortedInsert(DNode(2.5))
    clist.Print()

    # Demonstrate Delete functionality
    print("\nDeleting node with data value 1:")
    clist.Delete(node1)
    clist.Print()
        
    # Demonstrate insert functionality
    print("\nInserting new node with data value 0 at position 0:")
    clist.Insert(DNode(0), 0)
    clist.Print()
    
if __name__ == '__main__':
    main()
    
