from datastructures.Linear.singlyLL import Node, SinglyLL


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL(SinglyLL):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head:
            current = head
            while current.next:
                current = current.next
            self.tail = current
            self.size = 1

    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
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
            current.next.prev = node
            current.next = node
            node.prev = current
            self.size += 1

    def delete_head(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        temp.next = None
        self.size -= 1
        if not self.head:
            self.tail = None
        return temp

    def delete_tail(self):
        if not self.tail:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        temp.prev = None
        self.size -= 1
        if not self.tail:
            self.head = None
        return temp

    def delete_node(self, node):
        if not node or not self.head:
            return None

        # Delete the head node
        if self.head == node:
            return self.delete_head()

        # Delete the tail node
        if self.tail == node:
            return self.delete_tail()

        # Delete a node in the middle
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.size -= 1
        return node



# TESTING THE DLL:
def main():
    # Create some nodes
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)

    # Create a doubly linked list and insert some nodes
    dllist = DoublyLL()
    dllist.insert_head(node2)
    dllist.insert_head(node1)
    dllist.insert_tail(node3)

    # Print the list
    dllist.print()

    # Test the search function
    result = dllist.search(DNode(2))
    if result:
        print("Node found:", result.data)
    else:
        print("Node not found")

    # Test the delete function
    dllist.delete_node(DNode(2))
    dllist.print()

if __name__ == '__main__':
    main()
