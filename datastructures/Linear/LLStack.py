from SNode import Node
from singlyLL import SinglyLL

class LLStack(SinglyLL):
    def __init__(self, head=None):
        super().__init__(head)
        
    def push(self, node):
        self.insert_head(node)
    
    def pop(self):
        return self.delete_head()
    
    def peek(self):
        if self.head:
            return self.head.data
        return None
    
    def is_empty(self):
        return self.head is None
    
    def clear(self):
        super().clear()
    
    def print(self):
        if not self.head:
            print("Stack is empty.")
            return
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

