

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    
    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def insert_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
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
            current.next = node
            self.size += 1
    
    def sorted_insert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.size = 1
        elif node.data <= self.head.data:
            self.insert_head(node)
        elif node.data >= self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
    
    def search(self, node):
        current = self.head
        while current:
            if current.data == node.data:
                return current
            current = current.next
        return None


    
    def delete_head(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        if not self.head:
            self.tail = None
        return temp
    
    def delete_tail(self):
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
    
    def delete_node(self, node):
        if not node or not self.head:
            return None

        # Delete the head node
        if self.head.data == node.data:
            return self.delete_head()

        current = self.head
        prev = None
        while current:
            if current.data == node.data:
                break
            prev = current
            current = current.next

        # Node not found in linked list
        if not current:
            return None

        # Delete the tail node
        if current == self.tail:
            return self.delete_tail()

        # Delete a node in the middle
        prev.next = current.next
        current.next = None
        self.size -= 1
        return current



    
    def sort(self):
        if not self.head:
            return
        
        # Initialize the new list with the first node
        new_head = self.head
        new_tail = self.head
        current = self.head.next
        new_head.next = None
        
        # Traverse the original list
        while current:
            next_node = current.next
            
            # Insert the current node into the new list
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
        
        # Update the head and tail of the list
        self.head = new_head
        self.tail = new_tail


    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        if not self.head:
            print("List is empty.")
            return
        print("List length:", self.size)
        print("Sorted:", self.is_sorted())
        print("List content:")
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True



class LLQueue(SinglyLL):
    def __init__(self):
        super().__init__()

    def insert_head(self, node):
        pass

    def insert_tail(self, node):
        super().insert_tail(node)

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        else:
            super().insert(node, position)

    def sorted_insert(self, node):
        super().insert_tail(node)

    def search(self, node):
        return super().search(node)

    def delete_head(self):
        return super().delete_head()

    def delete_tail(self):
        return super().delete_tail()

    def delete_node(self, node):
        return super().delete_node(node)

    def sort(self):
        super().sort()

    def clear(self):
        super().clear()

    def enqueue(self, node):
        self.insert_tail(node)

    def dequeue(self):
        return self.delete_head()
    
    def print_queue(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    # Create a new LLQueue
    queue = LLQueue()

    # Add some nodes to the queue
    queue.enqueue(Node(1))
    queue.enqueue(Node(3))
    queue.enqueue(Node(2))

    # Print the queue
    print("Queue contents:", end=" ")
    queue.print_queue()

    # Dequeue some nodes from the queue
    print("Dequeuing", queue.dequeue().data)
    print("Dequeuing", queue.dequeue().data)

    # Print the queue again
    print("Queue contents:", end=" ")
    queue.print_queue()

    # Add some more nodes to the queue
    queue.enqueue(Node(4))
    queue.enqueue(Node(1))

    # Print the queue once more
    print("Queue contents:", end=" ")
    queue.print_queue()

if __name__ == '__main__':
    main()
