from SNode import Node
from singlyLL import SinglyLL

class CircularSinglyLL(SinglyLL):
    def __init__(self, node=None):
        if node:
            self.head = node
            self.tail = node
            node.next = node
            self.size = 1
        else:
            super().__init__()


    def is_empty(self):
        return self.size == 0

    def InsertHead(self, node):
        if self.is_empty():
            self.head = node
            self.tail = node
            node.next = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node
        self.size += 1

    
    def InsertTail(self, node):
        if self.is_empty():
            self.InsertHead(node)
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
            self.size += 1

    
    def Insert(self, node, position):
        if position < 0 or position > self.size:
            raise ValueError("Invalid position")
        elif position == 0:
            self.InsertHead(node)
        elif position == self.size:
            self.InsertTail(node)
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
    
    def DeleteHead(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        self.tail.next = self.head
        temp.next = None
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return temp

    
    def DeleteTail(self):
        if self.is_empty():
            return None
        current = self.head
        while current.next != self.tail:
            current = current.next
        temp = self.tail
        current.next = self.head
        self.tail = current
        self.size -= 1
        if self.is_empty():
            self.head = None
        return temp

    
    def Delete(self, position):
        if position < 0 or position >= self.size:
            raise ValueError("Invalid position")
        elif position == 0:
            return self.DeleteHead()
        elif position == self.size - 1:
            return self.DeleteTail()
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            temp = current.next
            current.next = temp.next
            temp.next = None
            self.size -= 1
            return temp
    
    def Search(self, node):
        if self.is_empty():
            return None
        current = self.head
        for i in range(self.size):
            if current.data == node.data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def length(self):
        return self.size

    
    def Clear(self):
        while not self.is_empty():
            self.DeleteHead()

        
    def is_sorted(self):
        if not self.tail:
            return True
        current = self.tail.next
        while current != self.tail:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    
    def Sort(self):
        if not self.head:
            return
        current = self.head
        while current.next != self.head:
            index = current.next
            while index != self.head:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next


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



# TESTING THE CLL:
def main():
    # Create a circular singly linked list with 3 nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    cll = CircularSinglyLL()
    cll.InsertTail(node1)
    cll.InsertTail(node2)
    cll.InsertHead(node3)
    
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()

    # Delete the head and tail nodes, and then print the list again
    cll.DeleteHead()
    cll.DeleteTail()
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()

    # Insert a new node at position 1, and then print the list again
    node4 = Node(4)
    cll.Insert(node4, 1)
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()

    # Sort the list and print it again
    cll.Sort()
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()

    # Clear the list and print it again
    cll.Clear()
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()

    # Test the search function
    cll.InsertTail(node1)
    cll.InsertTail(node2)
    cll.InsertTail(node3)
    node = Node(2)
    result = cll.Search(node)
    if result:
        print("Node found:", result.data)
    else:
        print("Node not found")
    print("List length:", cll.length())
    print("Sorted:", cll.is_sorted())
    print("List content:")
    cll.Print()


if __name__ == '__main__':
    main()

