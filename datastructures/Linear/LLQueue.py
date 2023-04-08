
from SNode import Node
from singlyLL import SinglyLL




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
