class TNode:
    def __init__(self, data=None, P=None, L=None, R=None, balance=0):
        self.data = data
        if isinstance(P, TNode) or P== None:
            self.parent = P
        else:
            raise TypeError("Parent must be a TNode object.")
        if isinstance(L, TNode) or L== None:
            self.left = L
        else:
            raise TypeError("Parent must be a TNode object.")
        if isinstance(R, TNode) or R== None:
            self.right = R
        else:
            raise TypeError("Parent must be a TNode object.")
        self.balance = balance

    def set_data(self, data):
        self.data = data
    
    def set_parent(self, parent):
        if isinstance(parent, TNode):
            self.parent = parent
        else:
            raise TypeError("Parent must be a TNode object.")
        
    def set_left(self, left):
        if isinstance(left, TNode):
            self.left = left
        else:
            raise TypeError("Left child must be a TNode object.")
        
    def set_right(self, right):
        if isinstance(right, TNode):
            self.right = right
        else:
            raise TypeError("Right child must be a TNode object.")
        
        
    def set_balance(self, balance):
        self.balance = balance

    def get_data(self):
        return self.data
    
    def get_parent(self):
        return self.parent
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def get_balance(self):
        return self.balance

    def toString(self):
        return str(self.data)

    def print_node(self):                 
        self.toString()
        print("This TNode's information:")
        print("Data:", self.data)
        if self.parent is not None:
            print("Parent:", self.parent.data)
        else:
            print("Parent: None")
        if self.left is not None:
            print("Left child:", self.left.data)
        else:
            print("Left child: None")
        if self.right is not None:
            print("Right child:", self.right.data)
        else:
            print("Right child: None")
        print("Balance:", self.balance)
