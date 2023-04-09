from SNode import Node
from singlyLL import SinglyLL

class LLStack(SinglyLL):
    def __init__(self, head=None):
        super().__init__(head)
        
    def push(self, node):
        self.InsertHead(node)
    
    def pop(self):
        return self.DeleteHead()
    
    def peek(self):
        if self.head:
            return self.head.data
        return None
    
    def is_empty(self):
        return self.head is None
    
    def clear(self):
        super().Clear()
    
    def print(self):
        if not self.head:
            print("Stack is empty.")
            return
        # Count the number of nodes in the list
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        # Check if the list is sorted
        is_sorted = True
        current = self.head
        while current.next:
            if current.data > current.next.data:
                is_sorted = False
                break
            current = current.next
        # Print the list information
        print("List length:", count)
        print("Sorted status:", "Yes" if is_sorted else "No")
        print("List content:")
        current = self.head
        while current:
            print(current.data)
            current = current.next



# Test the LLStack class
def main():
    stack = LLStack()
    # Push nodes onto the stack
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)

    # Print the stack
    stack.print()

    # Pop nodes from the stack
    print("Popped node:", stack.pop().data)
    print("Popped node:", stack.pop().data)

    # Print the stack
    stack.print()

    # Push a new node onto the stack
    node4 = Node(4)
    stack.push(node4)

    # Print the stack
    stack.print()

    # Clear the stack
    stack.clear()

    # Print the stack
    stack.print()


if __name__ == '__main__':
    main()

