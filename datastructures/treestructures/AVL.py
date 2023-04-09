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

    a = tree.search(1)
    a.print_node()
    a = tree.search(6)
    a.print_node()
    a = tree.search(7)
    a.print_node()
    a = tree.search(9)
    a.print_node()



if __name__ == '__main__':
    main()