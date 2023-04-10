from SNode import Node
from DNode import DNode
from LLStack import LLStack
from LLQueue import LLQueue
from singlyLL import SinglyLL
from doublyLL import DoublyLL
from singlyCLL import CircularSinglyLL
from doublyCLL import doublyCLL



def main():
# TESTING THE SINGLYLL:
    print("TESTING THE SINGLYLL")
    
    # create a singly linked list
    sll = SinglyLL()

    # insert nodes at head and tail
    sll.InsertHead(Node(2))
    sll.InsertHead(Node(4))
    sll.InsertHead(Node(1))
    sll.InsertTail(Node(5))

    # test printing the list
    sll.Print()  # should print 1, 4, 2, 5
    sll.Sort() 

    # test sorted insert
    sll.SortedInsert(Node(3))
    sll.SortedInsert(Node(0))
    sll.SortedInsert(Node(6))
    sll.Print()  # should print 0, 1, 2, 3, 4, 5, 6

    # test insert at position
    sll.Insert(Node(7), 7)
    sll.Insert(Node(-1), 0)
    sll.Print()  # should print -1, 0, 1, 2, 3, 4, 5, 6, 7

    # test search
    node = sll.Search(Node(3))
    if node:
        print("Node found:", node.data)  # should print "Node found: 3"
    else:
        print("Node not found")

    # test delete
    node = sll.Delete(Node(0))
    if node:
        print("Node deleted:", node.data)  # should print "Node deleted: 0"
    else:
        print("Node not found")
    sll.Delete(Node(7))
    sll.Delete(Node(6))
    sll.Print()  # should print -1, 1, 2, 3, 4, 5

    # test sort
    sll.InsertHead(Node(9))
    sll.Sort()
    sll.Print()  # should print -1, 1, 2, 3, 4, 5, 9

    # test clear
    sll.Clear()
    sll.Print()  # should print "List is empty."




# TESTING THE DOUBLYLL:
    print()
    print()
    print()
    print()

    print("TESTING THE DOUBLYLL")
    # Create some nodes
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    
    # Create an empty DoublyLL object
    dllist = DoublyLL()
    
    # Test InsertHead function
    dllist.InsertHead(node2)
    dllist.InsertHead(node1)
    dllist.Print() # should print 1 <-> 2
    
    # Test InsertTail function
    dllist.InsertTail(node3)
    dllist.Print() # should print 1 <-> 2 <-> 3
    
    # Test Insert function
    dllist.Insert(node4, 1)
    dllist.Print() # should print 1 <-> 4 <-> 2 <-> 3
    
    # Test DeleteHead function
    dllist.DeleteHead()
    dllist.Print() # should print 4 <-> 2 <-> 3
    
    # Test DeleteTail function
    dllist.DeleteTail()
    dllist.Print() # should print 4 <-> 2
    
    # Test Delete function
    dllist.Delete(node2)
    dllist.Print() # should print 4
    
    # Test Sort function
    node5 = DNode(5)
    node6 = DNode(6)
    node7 = DNode(7)
    dllist.InsertHead(node6)
    dllist.InsertTail(node5)
    dllist.InsertTail(node7)
    dllist.Print() # should print 6 <-> 4 <-> 5 <-> 7
    dllist.Sort()
    dllist.Print() # should print 4 <-> 5 <-> 6 <-> 7
    
    # Test Search function
    result = dllist.Search(DNode(6))
    if result:
        print("Node found:", result.data) # should print Node found: 6
    else:
        print("Node not found")
        
    result = dllist.Search(DNode(8))
    if result:
        print("Node found:", result.data)
    else:
        print("Node not found") # should print Node not found



# TESTING THE SINGLYCLL:
    print()
    print()
    print()
    print()
    print("TESTING THE SINGLYCLL")
    # Create a circular singly linked list with 3 nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    cll = CircularSinglyLL()
    cll.InsertTail(node1)
    cll.InsertTail(node2)
    cll.InsertHead(node3)

    # Print initial list information
    print("Initial list:")
    cll.Print()  # Expected output: 3 -> 1 -> 2 -> 3

    # Delete the head and tail nodes, and then print the list again
    cll.DeleteHead()
    cll.DeleteTail()
    print("List after deleting head and tail nodes:")
    cll.Print()  # Expected output: 1

    # Insert a new node at position 1, and then print the list again
    node4 = Node(4)
    cll.Insert(node4, 1)
    print("List after inserting node at position 1:")
    cll.Print()  # Expected output: 1 -> 4

    # Insert a new node at the head, and then print the list again
    node5 = Node(5)
    cll.InsertHead(node5)
    print("List after inserting node at the head:")
    cll.Print()  # Expected output: 5 -> 1 -> 4

    # Insert a new node at the tail, and then print the list again
    node6 = Node(6)
    cll.InsertTail(node6)
    print("List after inserting node at the tail:")
    cll.Print()  # Expected output: 5 -> 1 -> 4 -> 6

    # Delete the node at position 2, and then print the list again
    cll.Delete(2)
    print("List after deleting node at position 2:")
    cll.Print()  # Expected output: 5 -> 4 -> 6

    # Delete a non-existing node, and then print the list again
    cll.Delete(3)
    print("List after deleting non-existing node:")
    cll.Print()  # Expected output: 5 -> 4 -> 6

    # Clear the list and print the final list information
    cll.Clear()
    print("Final list after clearing the linked list:")
    cll.Print()  # Expected output: Empty list






# TESTING THE DOUBLYCLL:
    print()
    print()
    print()
    print()
    print("TESTING THE DOUBLYCLL")
    # Create nodes
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    node5 = DNode(5)

    # Create circular linked list
    clist = doublyCLL()
    print("Creating new circular linked list:")
    clist.Print()

    # Test is_empty method
    print("\nTesting is_empty method:")
    print("List is empty:", clist.is_empty())

    # Test InsertHead method
    print("\nTesting InsertHead method:")
    clist.InsertHead(node1)
    clist.Print()

    # Test InsertTail method
    print("\nTesting InsertTail method:")
    clist.InsertTail(node2)
    clist.Print()

    # Test Insert method
    print("\nTesting Insert method:")
    clist.Insert(node3, 1)
    clist.Print()

    # Test SortedInsert method
    print("\nTesting SortedInsert method:")
    clist.SortedInsert(node4)
    clist.Print()

    # Test is_sorted method
    print("\nTesting is_sorted method:")
    print("List is sorted:", clist.is_sorted())

    # Test length method
    print("\nTesting length method:")
    print("List length:", clist.length())

    # Test Search method
    print("\nTesting Search method:")
    result = clist.Search(node3)
    if result:
        print("Node found with data value 3")
    else:
        print("Node not found with data value 3")

    # Test DeleteHead method
    print("\nTesting DeleteHead method:")
    clist.DeleteHead()
    clist.Print()

    # Test DeleteTail method
    print("\nTesting DeleteTail method:")
    clist.DeleteTail()
    clist.Print()

    # Test Delete method
    print("\nTesting Delete method:")
    clist.Delete(node3)
    clist.Print()

    # Test edge cases
    print("\nTesting edge cases:")
    clist.InsertHead(node5)
    clist.InsertTail(node1)
    clist.DeleteHead()
    clist.DeleteTail()
    clist.Delete(node2)
    clist.Print()



# TESTING THE LLStack
    print()
    print()
    print()
    print()
    print("TESTING THE LLStack")    
    stack = LLStack()           # Initialize the stack

    # Test is_empty() function
    print("Is stack empty?", stack.is_empty())

    # Push nodes onto the stack
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    stack.push(node1)

    # Test push() and print() functions
    print("Pushed node:", node1.data)
    stack.print()

    stack.push(node2)
    stack.push(node3)

    # Test is_empty() function
    print("Is stack empty?", stack.is_empty())

    # Print the stack
    stack.print()

    # Test peek() function
    print("Peek:", stack.peek())

    # Push more nodes onto the stack
    stack.push(node4)
    stack.push(node5)

    # Test push() and print() functions
    print("Pushed node:", node4.data)
    stack.print()

    print("Pushed node:", node5.data)
    stack.print()

    # Test peek() function
    print("Peek:", stack.peek())

    # Test pop() function
    print("Popped node:", stack.pop().data)
    print("Popped node:", stack.pop().data)

    # Test pop() and print() functions
    stack.print()

    # Test clear() function
    stack.clear()

    # Test is_empty() function
    print("Is stack empty?", stack.is_empty())

    # Print the stack
    stack.print()

    # Push nodes onto the stack
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    stack.push(node6)

    # Test push() and print() functions
    print("Pushed node:", node6.data)
    stack.print()

    stack.push(node7)
    stack.push(node8)

    # Test is_empty() function
    print("Is stack empty?", stack.is_empty())

    # Print the stack
    stack.print()

    # Test peek() function
    print("Peek:", stack.peek())

    # Test pop() function
    print("Popped node:", stack.pop().data)

    # Test clear() function
    stack.clear()

    # Test is_empty() function
    print("Is stack empty?", stack.is_empty())

    # Print the stack
    stack.print()


# TESTING THE LLQUEUE
    print()
    print()
    print()
    print()
    print("TESTING THE LLQUEUE")    
    # Create a new LLQueue
    queue = LLQueue()

    # Add some nodes to the queue
    queue.enqueue(Node(1))
    queue.enqueue(Node(3))
    queue.enqueue(Node(2))

    # Print the queue
    print("Queue contents:", end=" ")
    queue.Print()

    # Dequeue some nodes from the queue
    print("Dequeuing", queue.dequeue().data)
    print("Dequeuing", queue.dequeue().data)

    # Print the queue again
    print("Queue contents:", end=" ")
    queue.Print()

    # Add some more nodes to the queue
    queue.enqueue(Node(4))
    queue.enqueue(Node(1))

    # Print the queue once more
    print("Queue contents:", end=" ")
    queue.Print()

    # Test the InsertHead function
    queue.InsertHead(Node(5))
    print("Inserting 5 at the head")
    queue.Print()

    # Test the insert function
    queue.insert(Node(6), 3)
    print("Inserting 6 at position 3")
    queue.Print()

    # Test the SortedInsert function
    queue.SortedInsert(Node(0))
    print("Inserting 0 in a sorted manner")
    queue.Print()

    # Test the Search function
    node_to_search = Node(4)
    search_result = queue.Search(node_to_search)
    if search_result is not None:
        print(f"Searching for {node_to_search.data}, Found: {search_result.data}")
    else:
        print(f"Node with data {node_to_search.data} not found")

    # Test the Delete function
    node_to_delete = Node(2)
    delete_result = queue.Delete(node_to_delete)
    if delete_result is not None:
        print(f"Deleting {node_to_delete.data}, Deleted: {delete_result.data}")
    else:
        print(f"Node with data {node_to_delete.data} not found")

    queue.Print()

    # Test the Sort function
    print("Sorting the list")
    queue.Sort()
    queue.Print()

    # Test the length function
    print(f"Length of the queue: {queue.length()}")

    # Test the Clear function
    print("Clearing the queue")
    queue.Clear()
    queue.Print()




if __name__ == '__main__':
    main()
