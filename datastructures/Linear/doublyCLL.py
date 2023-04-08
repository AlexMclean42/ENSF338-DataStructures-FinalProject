from DNode import DNode
from doublyLL import DoublyLL

class doublyCLL(DoublyLL):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
    
    def insert_head(self, node):
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
    
    def insert_tail(self, node):
        if not self.tail:
            self.insert_head(node)
        else:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        elif position >= self.size:
            self.insert_tail(node)
        else:
            current = self.head
            for i in range(1, position):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1
    
    def sorted_insert(self, node):
        if not self.head:
            self.insert_head(node)
        elif node.data <= self.head.data:
            self.insert_head(node)
        elif node.data >= self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1
    
    def search(self, node):
        current = self.head
        while current and current != self.tail:
            if current.data == node.data:
                return current
            current = current.next
        if current == self.tail and current.data == node.data:
            return current
        return None
    
    def delete_head(self):
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
    
    def delete_tail(self):
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
    
    def delete_node(self, node):
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
            self.delete_head()
        elif position == self.size - 1:
            self.delete_tail()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None
            self.size -= 1


def main():
    # Create nodes
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)

    # Create circular linked list
    clist = doublyCLL()
    clist.insert(node1, 0)
    clist.insert(node2, 1)
    clist.insert(node3, 2)

    # Print circular linked list
    print("Printing initial circular linked list:")
    current = clist.head
    while current:
        print(current.data)
        current = current.next
        if current == clist.head:
            break

    # Demonstrate search functionality
    print("\nSearching for node with data value 2:")
    result = clist.search(DNode(2))
    if result:
        print("Node found with data value 2")
    else:
        print("Node not found with data value 2")

    # Demonstrate sorted_insert functionality
    print("\nInserting new node with data value 2.5 in sorted order:")
    clist.sorted_insert(DNode(2.5))
    current = clist.head
    while current:
        print(current.data)
        current = current.next
        if current == clist.head:
            break

    # Demonstrate delete_node functionality
    print("\nDeleting node with data value 1:")
    clist.delete_node(node1)
    current = clist.head
    while current:
        print(current.data)
        current = current.next
        if current == clist.head:
            break
        
    # Demonstrate insert functionality
    print("\nInserting new node with data value 0 at position 0:")
    clist.insert(DNode(0), 0)
    current = clist.head
    while current:
        print(current.data)
        current = current.next
        if current == clist.head:
            break

    
if __name__ == '__main__':
    main()
