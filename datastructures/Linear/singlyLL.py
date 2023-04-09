from SNode import Node

class SinglyLL:
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

    def InsertHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def InsertTail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
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
            current.next = node
            self.size += 1

    def SortedInsert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.size = 1
        elif node.data <= self.head.data:
            self.InsertHead(node)
        elif node.data >= self.tail.data:
            self.InsertTail(node)
        else:
            current = self.head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
    
    def Search(self, node):
        current = self.head
        while current:
            if current.data == node.data:
                return current
            current = current.next
        return None



    def DeleteHead(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        if not self.head:
            self.tail = None
        return temp


    def DeleteTail(self):
        if not self.tail:
            return None
        current = self.head
        while current.next != self.tail:
            current = current.next
        temp = self.tail
        current.next = None
        self.tail = current
        self.size -= 1
        if not self.tail:
            self.head = None
        return temp


    def Delete(self, node):
        if not node or not self.head:
            return None
        if self.head.data == node.data:
            return self.DeleteHead()
        current = self.head
        prev = None
        while current:
            if current.data == node.data:
                break
            prev = current
            current = current.next
        if not current:
            return None
        if current == self.tail:
            return self.DeleteTail()
        prev.next = current.next
        current.next = None
        self.size -= 1
        return current



    
    def Sort(self):
        if not self.head:
            return
        new_head = self.head
        new_tail = self.head
        current = self.head.next
        new_head.next = None
        while current:
            next_node = current.next
            if current.data <= new_head.data:
                current.next = new_head
                new_head = current
            elif current.data >= new_tail.data:
                new_tail.next = current
                new_tail = current
                new_tail.next = None
            else:
                search = new_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            
            current = next_node
        self.head = new_head
        self.tail = new_tail


    def Clear(self):
        self.head = None
        self.tail = None
        self.size = 0


    def Print(self):
        if not self.head:
            print("List is empty.")
            return
        print("List length:", self.size)
        sorted_status = True
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                sorted_status = False
                break
            current = current.next
        print("Sorted:", sorted_status)
        print("List content:")
        current = self.head
        while current:
            print(current.data)
            current = current.next




# TESTING THE LL:
def main():
    # Create a singly linked list
    sll = SinglyLL()

    # Insert nodes at head and tail
    sll.InsertHead(Node(2))
    sll.InsertTail(Node(4))
    sll.InsertHead(Node(1))
    sll.InsertTail(Node(5))
    # sll.InsertHead(Node(3))


    # # Insert node at position
    sll.Insert(Node(3), 2)
    sll.Insert(Node(6), 1)
    sll.Print()


    # # Sort the list
    sll.Sort()

    # # Print the list
    sll.Print()

    # # Search for a node
    node = sll.Search(Node(4))
    if node:
        print("Node found:", node.data)
    else:
        print("Node not found")

    # # Delete a node
    node = sll.Delete(Node(3))
    if node:
        print("Node deleted:", node.data)
    else:
        print("Node not found")
    

    # # Clear the list
    sll.Clear()
    sll.Print()

if __name__ == '__main__':
    main()
