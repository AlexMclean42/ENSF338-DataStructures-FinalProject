from TNode import TNode
from BST import BST




class AVL(BST):
    def __init__(self, root=None):
        if root is None:
            self.root = None
        elif isinstance(root, int):
            self.root = TNode(root)
        elif isinstance(root, TNode):
            # self.root = root
            self.root = self.balance(root)


    def balance(self, node):
        """
        Balances the subtree rooted at the given node using AVL method.

        Parameters:
        node (TNode): The root node of the subtree to be balanced.

        Returns:
        The new root node of the subtree after balancing.
        """
        if node is None:
            return None

        # recursively balance the left and right subtrees
        node.left = self.balance(node.left)
        node.right = self.balance(node.right)

        # update the balance factor of the node
        node.balance = self.height(node.right) - self.height(node.left)

        # if the node is unbalanced, perform rotations
        if node.balance > 1:  # right heavy
            if node.right.balance < 0:  # right-left case
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)  # right-right case
        elif node.balance < -1:  # left heavy
            if node.left.balance > 0:  # left-right case
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)  # left-left case

        # if the node is already balanced, return it
        return node

    def height(self, node):
        """
        Calculates the height of the subtree rooted at the given node.

        Parameters:
        node (TNode): The root node of the subtree.

        Returns:
        The height of the subtree.
        """
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left), self.height(node.right))



    def rotate_left(self, node):
        """
        Performs a left rotation on the subtree rooted at the given node.

        Parameters:
        node (TNode): The root node of the subtree to be rotated.

        Returns:
        The new root node of the subtree after the rotation.
        """
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node
        new_root.left = node
        new_root.parent = node.parent
        node.parent = new_root

        # update balance factors
        node.balance = self.height(node.right) - self.height(node.left)
        new_root.balance = self.height(new_root.right) - self.height(new_root.left)

        return new_root



    def rotate_right(self, node):
        """
        Performs a right rotation on the subtree rooted at the given node.

        Parameters:
        node (TNode): The root node of the subtree to be rotated.

        Returns:
        The new root node of the subtree after the rotation.
        """
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node
        new_root.right = node
        new_root.parent = node.parent
        node.parent = new_root

        # update balance factors
        node.balance = self.height(node.right) - self.height(node.left)
        new_root.balance = self.height(new_root.right) - self.height(new_root.left)

        return new_root





    # def Insert(self, val):
    #     node = super().Insert(val)
    #     # self.balance_AVL(node)

    #     node = TNode(val)
    #     if self.root is None:
    #         self.root = node
    #         return
    #     current = self.root
    #     while current is not None:
    #         if val < current.data:
    #             if current.left is None:
    #                 current.left = node
    #                 node.parent = current
    #                 break
    #             current = current.left
    #         else:
    #             if current.right is None:
    #                 current.right = node
    #                 node.parent = current
    #                 break
    #             current = current.right
    #     # balance the tree from the parent of the inserted node up to the root
    #     while node is not None:
    #         node = self.balance_AVL(node.parent)


def main():                       #Test main delete before submission
    #node = TNode(1, TNode(2, TNode(4), TNode(5)), TNode(3, TNode(6), TNode(7)))
    #node = TNode(3, L=TNode(2, L=TNode(1, L=TNode(0))))
    ahh = BST()
    # ahh.Insert(4)
    # ahh.Insert(2)
    # ahh.Insert(3)
    ahh.Insert(1)
    ahh.Insert(6)
    ahh.Insert(7)
    ahh.Insert(9)
    


    tree = AVL(ahh.root)

    # Print the contents of the tree in ascending order
    print("Contents of tree in ascending order:")
    tree.printInOrder()
    print()

    # Print the contents of the tree in Breadth-First order
    print("Contents of tree in Breadth-First order:")
    tree.printBF()

    # bst.Delete(5)

    # # Print the contents of the bst in ascending order
    # print("Contents of bst in ascending order:")
    # bst.printInOrder()
    # print()

    # # Print the contents of the bst in Breadth-First order
    # print("Contents of tree in Breadth-First order:")
    # tree.printBF()


    a = tree.search(1)
    a.print_node()
    a = tree.search(7)
    a.print_node()
    a = tree.search(6)
    a.print_node()
    a = tree.search(9)
    a.print_node()
    a = tree.search(4)
    # a.print_node()
    # a = tree.search(3)
    # a.print_node()
    # a = tree.search(2)
    # a.print_node()

    


if __name__ == '__main__':
    main()




    # def balance_tree(self, node):
    #     if node is None:
    #         return None
        
    #     node.left = self.balance_tree(node.left)
    #     node.right = self.balance_tree(node.right)
        
    #     balance_factor = self.get_balance_factor(node)
        
    #     if balance_factor > 1:
    #         if self.get_balance_factor(node.left) < 0:
    #             node.left = self.rotate_left(node.left)
    #         node = self.rotate_right(node)
    #     elif balance_factor < -1:
    #         if self.get_balance_factor(node.right) > 0:
    #             node.right = self.rotate_right(node.right)
    #         node = self.rotate_left(node)
        
    #     if node == self.root:
    #         self.root = node

    #     return node
    
    # def get_balance_factor(self, node):
    #     if node is None:
    #         return 0
    #     return self.get_height(node.left) - self.get_height(node.right)
    
    # def get_height(self, node):
    #     if node is None:
    #         return 0
    #     return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    # def rotate_left(self, node):
    #     new_root = node.right
    #     node.right = new_root.left
    #     new_root.left = node
    #     return new_root
    
    # def rotate_right(self, node):
    #     new_root = node.left
    #     node.left = new_root.right
    #     new_root.right = node
    #     return new_root




# class AVL(BST):
#     def __init__(self, root=None):
#         super().__init__(root)
#         self._assign_balance(self.get_root())

#     def _assign_balance(self, node):
#         """
#         Recursive helper function to assign balance to each node in the bst.
#         """
#         if node is None:
#             return
        
#         # Recursively assign balance to left and right subtrees
#         self._assign_balance(node.get_left())
#         self._assign_balance(node.get_right())
        
#         # Calculate balance of current node
#         balance = self.get_height(node.get_left()) - self.get_height(node.get_right())
#         node.set_balance(balance)

#     def get_height(self, node):
#         if node is None:
#             return -1
#         return 1 + max(self.get_height(node.get_left()), self.get_height(node.get_right()))


#     def insert(self, valOrNode):
#         self._assign_balance(self.get_root())
#         node = None
#         if isinstance(valOrNode, int):
#             node = TNode(valOrNode)
#         elif isinstance(valOrNode, TNode):
#             node = valOrNode
#         else:
#             raise TypeError("Value must be an integer or TNode object.")
#         super().Insert(node)
#         self.balance(node)
    
#     def balance(self, node):
#         if node is None:
#             return
#         if node.get_balance() > 1:
#             if node.get_left() and node.get_left().get_balance() < 0:
#                 self.left_rotate(node.get_left())
#             self.right_rotate(node)
#         elif node.get_balance() < -1:
#             if node.get_right() and node.get_right().get_balance() > 0:
#                 self.right_rotate(node.get_right())
#             self.left_rotate(node)
#         self.balance(node.get_parent())
        
#     def left_rotate(self, node):
#         new_root = node.get_right()
#         node.set_right(new_root.get_left())
#         if new_root.get_left():
#             new_root.get_left().set_parent(node)
#         new_root.set_parent(node.get_parent())
#         if not node.get_parent():
#             self.set_root(new_root)
#         elif node == node.get_parent().get_left():
#             node.get_parent().set_left(new_root)
#         else:
#             node.get_parent().set_right(new_root)
#         new_root.set_left(node)
#         node.set_parent(new_root)
#         node.set_balance(node.get_balance() + 1 - min(new_root.get_balance(), 0))
#         new_root.set_balance(new_root.get_balance() + 1 + max(node.get_balance(), 0))
    
#     def right_rotate(self, node):
#         new_root = node.get_left()
#         node.set_left(new_root.get_right())
#         if new_root.get_right():
#             new_root.get_right().set_parent(node)
#         new_root.set_parent(node.get_parent())
#         if not node.get_parent():
#             self.set_root(new_root)
#         elif node == node.get_parent().get_right():
#             node.get_parent().set_right(new_root)
#         else:
#             node.get_parent().set_left(new_root)
#         new_root.set_right(node)
#         node.set_parent(new_root)
#         node.set_balance(node.get_balance() + 1 - min(new_root.get_balance(), 0))
#         new_root.set_balance(new_root.get_balance() + 1 + max(node.get_balance(), 0))
    
#     def delete(self, val):
#         node = self.search(val)
#         if node:
#             super().delete(node)
#             self.balance(node.get_parent())
#         else:
#             print("Value not found in bst.")




# class AVLNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.balance = 0

# class AVLTree:
#     def __init__(self):
#         self.root = None
    
#     def get_balance(self, node):
#         if node is None:
#             return 0
#         return node.balance
    
#     def set_balance(self, node):
#         node.balance = self.height(node.right) - self.height(node.left)
    
#     def right_rotate(self, node):
#         new_root = node.left
#         node.left = new_root.right
#         new_root.right = node
#         self.set_balance(node)
#         self.set_balance(new_root)
#         return new_root
    
#     def left_rotate(self, node):
#         new_root = node.right
#         node.right = new_root.left
#         new_root.left = node
#         self.set_balance(node)
#         self.set_balance(new_root)
#         return new_root
    
#     def rebalance(self, node):
#         self.set_balance(node)
#         if node.balance == -2:
#             if self.get_balance(node.left) > 0:
#                 node.left = self.left_rotate(node.left)
#             return self.right_rotate(node)
#         elif node.balance == 2:
#             if self.get_balance(node.right) < 0:
#                 node.right = self.right_rotate(node.right)
#             return self.left_rotate(node)
#         return node
    
#     def insert(self, val):
#         def _insert(node, val):
#             if node is None:
#                 return AVLNode(val)
#             if val < node.val:
#                 node.left = _insert(node.left, val)
#             elif val > node.val:
#                 node.right = _insert(node.right, val)
#             return self.rebalance(node)
#         self.root = _insert(self.root, val)


# def __init__(self, root=None):
#         if root is None:
#             self.root = None
#         elif isinstance(root, int):
#             self.root = TNode(root)
#         elif isinstance(root, TNode):
#             self.root = root
#             if self.root.left is not None or self.root.right is not None:
#                 self.root = self.rebalance(self.root)




# class AVL(BST):
#     def __init__(self, root=None):
#         super().__init__(root)
#         self.root = self.rebalance(root)


#     def height(self, node):
#         if node is None:
#             return -1
#         return 1 + max(self.height(node.left), self.height(node.right))
    

#     def get_balance(self, node):
#         if node is None:
#             return 0
#         return node.balance
    
#     def set_balance(self, node):
#         node.balance = self.height(node.right) - self.height(node.left)
    
#     def right_rotate(self, node):
#         new_root = node.left
#         node.left = new_root.right
#         new_root.right = node
#         self.set_balance(node)
#         self.set_balance(new_root)
#         return new_root
    
#     def left_rotate(self, node):
#         new_root = node.right
#         node.right = new_root.left
#         new_root.left = node
#         self.set_balance(node)
#         self.set_balance(new_root)
#         return new_root
    
#     def rebalance(self, node):
#         self.set_balance(node)
#         if node.balance == -2:
#             if self.get_balance(node.left) > 0:
#                 node.left = self.left_rotate(node.left)
#             return self.right_rotate(node)
#         elif node.balance == 2:
#             if self.get_balance(node.right) < 0:
#                 node.right = self.right_rotate(node.right)
#             return self.left_rotate(node)
#         return node
    
#     def insert(self, val):
#         def _insert(node, val):
#             if node is None:
#                 return AVL(val)
#             if val < node.val:
#                 node.left = _insert(node.left, val)
#             elif val > node.val:
#                 node.right = _insert(node.right, val)
#             return self.rebalance(node)
#         self.root = _insert(self.root, val)



    # def balance(self, node):
    #     """
    #     Helper function to balance an AVL bst starting at a given node.
    #     """
    #     # Calculate the balance factor of the node
    #     balance_factor = self.balance_factor(node)

    #     # If the node is left-heavy
    #     if balance_factor > 1:
    #         # If the left child is right-heavy, perform a left rotation on it
    #         if self.balance_factor(node.left) < 0:
    #             node.left = self.rotate_left(node.left)

    #         # Perform a right rotation on the node
    #         node = self.rotate_right(node)

    #     # If the node is right-heavy
    #     elif balance_factor < -1:
    #         # If the right child is left-heavy, perform a right rotation on it
    #         if self.balance_factor(node.right) > 0:
    #             node.right = self.rotate_right(node.right)

    #         # Perform a left rotation on the node
    #         node = self.rotate_left(node)

    #     return node


    # def rotate_right(self, node):
    #     new_root = node.left
    #     node.left = new_root.right
    #     new_root.right = node
    #     return new_root

    # def rotate_left(self, node):
    #     new_root = node.right
    #     node.right = new_root.left
    #     new_root.left = node
    #     return new_root


# from TNode import TNode
# from BST import BST


# class AVL(BST):
#     def __init__(self, root=None):
#         super().__init__(root)
        
#     def insert(self, valOrNode):
#         node = None
#         if isinstance(valOrNode, int):
#             node = TNode(valOrNode)
#         elif isinstance(valOrNode, TNode):
#             node = valOrNode
#         else:
#             raise TypeError("Value must be an integer or TNode object.")
#         super().Insert(node)
#         self.balance(node)
    


#     def balance(self, node):
#         if node is None:
#             return
#         while node is not None:
#             node.set_balance(node.get_height())
#             if node.get_balance() > 1:
#                 if node.get_left() and node.get_left().get_balance() < 0:
#                     self.left_rotate(node.get_left())
#                 self.right_rotate(node)
#             elif node.get_balance() < -1:
#                 if node.get_right() and node.get_right().get_balance() > 0:
#                     self.right_rotate(node.get_right())
#                 self.left_rotate(node)
#             node = node.get_parent()

        
#     def left_rotate(self, node):
#         new_root = node.get_right()
#         node.set_right(new_root.get_left())
#         if new_root.get_left():
#             new_root.get_left().set_parent(node)
#         new_root.set_parent(node.get_parent())
#         if not node.get_parent():
#             self.set_root(new_root)
#         elif node == node.get_parent().get_left():
#             node.get_parent().set_left(new_root)
#         else:
#             node.get_parent().set_right(new_root)
#         new_root.set_left(node)
#         node.set_parent(new_root)
#         node.set_balance(node.get_balance() + 1 - min(new_root.get_balance(), 0))
#         new_root.set_balance(new_root.get_balance() + 1 + max(node.get_balance(), 0))
    
#     def right_rotate(self, node):
#         new_root = node.get_left()
#         node.set_left(new_root.get_right())
#         if new_root.get_right():
#             new_root.get_right().set_parent(node)
#         new_root.set_parent(node.get_parent())
#         if not node.get_parent():
#             self.set_root(new_root)
#         elif node == node.get_parent().get_right():
#             node.get_parent().set_right(new_root)
#         else:
#             node.get_parent().set_left(new_root)
#         new_root.set_right(node)
#         node.set_parent(new_root)
#         node.set_balance(node.get_balance() + 1 - min(new_root.get_balance(), 0))
#         new_root.set_balance(new_root.get_balance() + 1 + max(node.get_balance(), 0))
    
#     def delete(self, val):
#         node = self.search(val)
#         if node:
#             super().delete(node)
#             self.balance(node.get_parent())
#         else:
#             print("Value not found in bst.")

# class AVL(BST):

#     def __init__(self, root=None):
#         super().__init__(root)
    
#     def _rotate_left(self, node):
#        .right = node.right
#         node.right =.right.left
#         if.right.left is not None:
#            .right.left.parent = node
#        .right.parent = node.parent
#         if node.parent is None:
#             self.root =.right
#         elif node == node.parent.left:
#             node.parent.left =.right
#         else:
#             node.parent.right =.right
#        .right.left = node
#         node.parent =.right
#         node.balance += 1
#        .right.balance += 1
    
#     def _rotate_right(self, node):
#         left = node.left
#         node.left = left.right
#         if left.right is not None:
#             left.right.parent = node
#         left.parent = node.parent
#         if node.parent is None:
#             self.root = left
#         elif node == node.parent.right:
#             node.parent.right = left
#         else:
#             node.parent.left = left
#         left.right = node
#         node.parent = left
#         node.balance -= 1
#         left.balance -= 1
    
#     def _rotate_left_right(self, node):
#         self._rotate_left(node.left)
#         self._rotate_right(node)
    
#     def _rotate_right_left(self, node):
#         self._rotate_right(node.right)
#         self._rotate_left(node)
    
#     def Insert(self, valOrNode):
#         if isinstance(valOrNode, int):
#             node = TNode(valOrNode)
#         elif isinstance(valOrNode, TNode):
#             node = valOrNode
#         else:
#             raise TypeError("Insert argument must be an integer or a TNode object.")
        
#         if self.root is None:
#             self.root = node
#         else:
#             current = self.root
#             parent = None
#             while current is not None:
#                 parent = current 
#                 if node.data <= current.data:
#                     current = current.left
#                 else:
#                     current = current.right

#             if node.data <= parent.data:
#                 parent.left = node
#                 node.parent = parent
#                 parent.balance += 1
#             else:
#                 parent.right = node
#                 node.parent = parent
#                 parent.balance -= 1

#             if abs(parent.balance) == 2:
#                 if parent.balance == 2 and node.data < parent.left.data:
#                     self._rotate_right(parent)
#                 elif parent.balance == 2 and node.data > parent.left.data:
#                     self._rotate_left_right(parent)
#                 elif parent.balance == -2 and node.data > parent.right.data:
#                     self._rotate_left(parent)
#                 else:
#                     self._rotate_right_left(parent)
                
#                 if parent.parent is not None:
#                     parent = parent.parent
#                     if parent.left == node:
#                         parent.balance += 1
#                     else:
#                         parent.balance -= 1
#                     if abs(parent.balance) == 2:
#                         if parent.balance == 2 and node.data < parent.left.data:
#                             self._rotate_right(parent)
#                         elif parent.balance == 2 and node.data > parent.left.data:
#                             self._rotate_left_right(parent)
#                         elif parent.balance == -2 and node.data > parent.right.data:
#                             self._rotate_left(parent)
#                         else:
#                             self._rotate_right_left(parent)

