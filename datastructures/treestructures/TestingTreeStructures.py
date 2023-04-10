from TNode import TNode
from BST import BST
from AVL import AVL 


def main(): 
    print("\nBeginning of Tree Structure tests!")
    """
    Tests for TNode
    """

    print("\n\nTest constructor with no arguments and test getters:")
    default_constructor = TNode()
    print("\nExpected None: ", str(default_constructor.get_data()))
    print("Expected None: ", str(default_constructor.get_parent()))
    print("Expected None: ", str(default_constructor.get_left()))
    print("Expected None: ", str(default_constructor.get_right()))
    print("Expected 0: ", str(default_constructor.get_balance()))

    print("\n\nTest set_data (helps for next test):")
    default_constructor.set_data(1)
    print("\nExpected 1: ", str(default_constructor.get_data()))

    print("\n\nTest constructor with arguments and test getters:")
    arguments_constructor = TNode(data=338, P=default_constructor, L=TNode(100), R=TNode(400), balance=0)
    print("\nExpected 338: ", str(arguments_constructor.get_data()))
    print("Expected 1: ", arguments_constructor.get_parent().toString())
    print("Expected 100: ", arguments_constructor.get_left().toString())
    print("Expected 400: ", arguments_constructor.get_right().toString())
    print("Expected 0: ", str(arguments_constructor.get_balance()))

    print("\n\nTest setters and print_node:")
    setters_printNode_test = TNode()
    setters_printNode_test.set_data(5)
    setters_printNode_test.set_right(TNode(6))
    setters_printNode_test.set_parent(TNode(9))
    setters_printNode_test.set_balance(1)

    print()
    setters_printNode_test.print_node()

    print("\n\nTest intializing and setting parents or children that aren't TNodes:")
    print("\nExpected: Child must be a TNode object:")
    initialize_wrong_child_type = TNode(data=338, P=default_constructor, L=TNode(100), R=400, balance=0)
    
    print("\nExpected: Parent must be a TNode object:")
    initialize_wrong_parent_type = TNode(data=338, P=11, L=TNode(100), R=TNode(400), balance=0)

    set_wrong_child_type = TNode()
    print("\nExpected: Left child must be a TNode object:")
    set_wrong_child_type.set_left(11)

    set_wrong_parent_type = TNode()
    print("\nExpected: Parent must be a TNode object:")
    set_wrong_parent_type.set_parent(11)

    print("\n\nTest toString:")
    toString_test = TNode(2, TNode(9), TNode(1), TNode(3), 0)
    print("\nExpected 9: ", toString_test.parent.toString())
    print("Expected 1: ", toString_test.left.toString())
    print("Expected 3: ", toString_test.right.toString())


    """
    Tests for BST
    """

    print("\n\nTest constructor with no argument:")
    default_constructor = BST()
    print("\nExpected None: ", default_constructor.root) 

    print("\n\nTest constructor with int argument:")
    int_constructor = BST(7)
    print("\nExpected 7: ", int_constructor.root.get_data()) 
    print("Expected None: ", int_constructor.root.get_left()) 
    print("Expected None: ", int_constructor.root.get_right()) 

    print("\n\nTest constructor with TNode argument:")
    temp = TNode(data=7, P=None, L=TNode(6), R=TNode(8), balance=0)

    TNode_constructor = BST(temp)
    print("\nExpected 7: ", TNode_constructor.root.get_data()) 
    print("Expected 6: ", TNode_constructor.root.get_left().toString()) 
    print("Expected 8: ", TNode_constructor.root.get_right().toString()) 

    print("\n\nTest setter and getter:")
    setter_getter_int = BST()
    setter_getter_int.set_root(5)
    print("\nExpected 5: ", setter_getter_int.get_root().toString())

    setter_getter_int = BST()
    setter_getter_int.set_root(TNode(20))
    print("Expected 20: ", setter_getter_int.get_root().toString())

    print("\n\nTest setting root when root has already been set_get:")
    setter_getter_int = BST(TNode(10))
    print("Expected A root has already been set_get: ") 
    setter_getter_int.set_root(TNode(25))

    print("\n\nTest Insert val with without initialized root and test printBF() function:")
    tree_without_root = BST()

    tree_without_root.Insert(10)
    tree_without_root.Insert(20)
    tree_without_root.Insert(5)
    tree_without_root.Insert(1)
    tree_without_root.Insert(6)
    tree_without_root.Insert(11)
    tree_without_root.Insert(16)

    print("\nExpecteed: \n10\n5 20\n1 6 11\n16\n")
    tree_without_root.printBF()

    print("\n\nTest Insert val with with initialized root and test search() function:")
    tree_with_root = BST()

    tree_with_root.Insert(10)
    tree_with_root.Insert(15)
    tree_with_root.Insert(12)
    tree_with_root.Insert(17)
    tree_with_root.Insert(5)
    tree_with_root.Insert(1)

    ten = tree_with_root.search(10)
    print("\nExpected Data: 10, Parent: None, Left Child: 5, Right Child: 15, Balance: 0")
    ten.print_node()

    fifteen = tree_with_root.search(15)
    print("\nExpected Data: 15, Parent: 10, Left Child: 12, Right Child: 17, Balance: 0")
    fifteen.print_node()

    twelve = tree_with_root.search(12)
    print("\nExpected Data: 12, Parent: 15, Left Child: None, Right Child: None, Balance: 0")
    twelve.print_node()

    seventeen = tree_with_root.search(17)
    print("\nExpected Data: 17, Parent: 15, Left Child: None, Right Child: None, Balance: 0")
    seventeen.print_node()

    five = tree_with_root.search(5)
    print("\nExpected Data: 5, Parent: 10, Left Child: 1, Right Child: None, Balance: 0")
    five.print_node()

    one = tree_with_root.search(1)
    print("\nExpected Data: 1, Parent: 5, Left Child: None, Right Child: None, Balance: 0")
    one.print_node()

    print("\n\nTest insert TNode:")
    insert_TNode = BST()
    insert_TNode.Insert(TNode(2))
    insert_TNode.Insert(TNode(1))
    insert_TNode.Insert(TNode(0))
    insert_TNode.Insert(TNode(4))
    insert_TNode.Insert(TNode(3))
    print("\nExpecteed: \n2\n1 4\n0 3\n")
    insert_TNode.printBF()

    tree_with_root.Insert(TNode(13, L=TNode(12.5), R=TNode(14)))
    print("\nExpecteed: \n10\n5 15\n1 12 17\n13\n12.5 14\n")
    tree_with_root.printBF()

    print("\n\nTest Delete:")
    delete_nodes = tree_with_root

    print("Delete a node with no children:")
    delete_nodes.Delete(12.5)
    print("\nExpected 12.5 gone:")    
    delete_nodes.printBF()

    print("\nDelete a node with children and a parent:")
    delete_nodes.Delete(12)
    print("\nExpected 12 gone:")      
    delete_nodes.printBF()
    print("\nTo show properly deleted node 13's parent should be 15 and right child should be 14:")
    print("Expected 15:", delete_nodes.search(13).get_parent().toString())
    print("Expected 14:", delete_nodes.search(13).get_right().toString())

    print("\nDelete root node:")
    delete_nodes.Delete(10)
    print("\nExpected 10 gone:")    
    delete_nodes.printBF()

    print("\n\nTest delete with value not found:")
    print("\nExpected 'Value was not found in the insert_node.':")
    delete_nodes.Delete(100)
    
    print("\n\nTest delete with double value:")
    delete_nodes.Insert(13)
    delete_nodes.Insert(13)
    print("\nAfter duplicate 13's inserted:")
    delete_nodes.printBF()
    delete_nodes.Delete(13)
    print("Expected all 13's gone:")
    delete_nodes.printBF()

    print("\n\nTest print in order:")
    order = insert_TNode
    print("\nExpected 0 1 2 3 4:")
    order.printInOrder()


    """
    Tests for AVL
    """

    print("\n\nTest constructor with no argument:")
    default_constructor = AVL()
    print("\n\nExpected None: ", default_constructor.root) 
    
    print("\n\nTest constructor with int argument:")
    int_constructor = BST(7)
    print("\nExpected 7: ", int_constructor.root.get_data()) 
    print("Expected None: ", int_constructor.root.get_left()) 
    print("Expected None: ", int_constructor.root.get_right()) 

    print("\n\nTest constructor with TNode argument:")
    temp = TNode(data=7, P=None, L=TNode(6), R=TNode(8), balance=0)

    TNode_constructor = BST(temp)
    print("\nExpected 7: ", TNode_constructor.root.get_data()) 
    print("Expected 6: ", TNode_constructor.root.get_left().toString()) 
    print("Expected 8: ", TNode_constructor.root.get_right().toString()) 

    print("\n\nTest constructor with TNode argument that is the head of a BST insert_node, requiring full balancing algorithm:")
    print("Additionally testing printBF() inherited from BST:")
    BST_tree = BST(10)
    BST_tree.Insert(9)
    BST_tree.Insert(8)
    BST_tree.Insert(7)
    BST_tree.Insert(6)
    BST_tree.Insert(5)
    print("\nTree as a BST:")
    BST_tree.printBF()
    print("Tree as an AVL, should be balanced with 10 no longer the root:")
    TNode_arg_constructor = AVL(BST_tree.root)
    TNode_arg_constructor.printBF()

    print("\n\nTest that newly balanced insert_node's nodes have properly edited members:.")
    print("Additionally test search() inherited from BST:")
    print("\nCheck each node is updated properly:")

    eight = TNode_arg_constructor.search(8)
    print("\nExpected Data: 8, Parent: None, Left Child: 6, Right Child: 10, Balance: 0")
    eight.print_node()

    six = TNode_arg_constructor.search(6)
    print("\nExpected Data: 6, Parent: 8, Left Child: 5, Right Child: 7, Balance: 0")
    six.print_node()

    ten = TNode_arg_constructor.search(10)
    print("\nExpected Data: 10, Parent: 8, Left Child: 9, Right Child: None, Balance: -1")
    ten.print_node()

    five = TNode_arg_constructor.search(5)
    print("\nExpected Data: 5, Parent: 6, Left Child: None, Right Child: None, Balance: 0")
    five.print_node()

    seven = TNode_arg_constructor.search(7)
    print("\nExpected Data: 7, Parent: 6, Left Child: None, Right Child: None, Balance: 0")
    seven.print_node()

    nine = TNode_arg_constructor.search(9)
    print("\nExpected Data: 9, Parent: 10, Left Child: None, Right Child: None, Balance: 0")
    nine.print_node()


    print("\n\nTest setter:")
    BST_tree2 = BST(10)
    BST_tree2.Insert(9)
    BST_tree2.Insert(8)
    BST_tree2.Insert(14)
    BST_tree2.Insert(15)
    BST_tree2.Insert(16)
    BST_tree2.Insert(20)
    set_get = AVL()
    print("\nTree as a BST:")
    BST_tree2.printBF()
    set_get.set_root(BST_tree2.root)
    print("\nTree as AVL, should be balanced with 10 no longer the root:")
    set_get.printBF()

    print("\n\nTest balance values are correct for nodes and show that none exceed -1 or 1:")
    print("\nExpected 1: ", set_get.search(10).get_balance())
    print("Expected -1: ", set_get.search(9).get_balance())
    print("Expected -1: ", set_get.search(16).get_balance())
    print("Expected 0: ", set_get.search(8).get_balance())
    print("Expected 1: ", set_get.search(14).get_balance())
    print("Expected 0: ", set_get.search(20).get_balance())
    print("Expected 0: ", set_get.search(15).get_balance())

    print("\n\nTest getter:")
    print("\nExpected 10: ", set_get.get_root().toString())

    print("\n\nTest insert with int val with no root argument constructor:")
    insert_val = AVL()
    insert_val.Insert(4)
    insert_val.Insert(2)
    insert_val.Insert(3)
    insert_val.Insert(1)
    insert_val.Insert(5)
    insert_val.Insert(7)
    insert_val.Insert(9)
    print("\nExpected: \n3\n2 5\n1 4 7\n9")
    print("Result:")
    insert_val.printBF()

    print("\n\nTest insert with TNode node with root argument constructor:")
    insert_node = AVL(TNode(4))
    insert_node.Insert(TNode(2))
    insert_node.Insert(TNode(1))
    insert_node.Insert(TNode(5))
    insert_node.Insert(TNode(7))
    insert_node.Insert(TNode(9))
    insert_node.Insert(TNode(6))
    insert_node.Insert(TNode(8))
    insert_node.Insert(TNode(3))
    insert_node.Insert(TNode(0)) 
    print("\nExpected:\n5\n2 7\n1 4 6 9\n0 3 8")
    print("Result:")
    insert_node.printBF()

    print("\n\nTest Delete:")
    delete_nodes = insert_node

    print("Delete a node with no children:")
    delete_nodes.Delete(6)
    print("\nExpected 6 gone:")    
    delete_nodes.printBF()

    print("\nDelete a node with children and a parent:")
    delete_nodes.Delete(2)
    print("\nExpected 2 gone:")      
    delete_nodes.printBF()

    print("\nDelete root node:")
    delete_nodes.Delete(5)
    print("\nExpected 5 gone:")    
    delete_nodes.printBF()

    print("\n\nTest after deletions all nodes still have a balance between -1 and 1:")
    print("\nExpected -1: ", delete_nodes.search(7).get_balance())
    print("Expected -1: ", delete_nodes.search(3).get_balance())
    print("Expected 1: ", delete_nodes.search(8).get_balance())
    print("Expected -1: ", delete_nodes.search(1).get_balance())
    print("Expected 0: ", delete_nodes.search(4).get_balance())
    print("Expected 0: ", delete_nodes.search(9).get_balance())
    print("Expected 0: ", delete_nodes.search(0).get_balance())

    print("\n\nTest delete with value not found:")
    print("\nExpected 'Value was not found in the insert_node.':")
    delete_nodes.Delete(100)
    
    print("\n\nTest delete with double value:")
    delete_nodes.Insert(3)
    delete_nodes.Insert(3)
    print("\nAfter duplicate 3's inserted:")
    delete_nodes.printBF()
    delete_nodes.Delete(3)
    print("Expected all 3's gone:")
    delete_nodes.printBF()

    print("\n\nTest print in order:")
    order = insert_val
    print("\nExpected 1 2 3 4 7 9:")
    order.printInOrder()
    
    
    print("\n\nEnd of Tree Structure Tests!")



if __name__ == '__main__':
    main()