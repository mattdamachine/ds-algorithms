'''Average running time complexity: O(log(n))
   Worst case (in the event of an unbalanced tree): O(n)
   Generally faster than a list'''

class TreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def insert(self, value):
        '''Add a node to the tree with specified value'''
        # If a value is less than the current node, we go left. Otherwise we go right.
        if value < self.value:
            if self.left is None:  # Is there a left child?
                self.left = TreeNode(value, self)
            else:
                self.left.insert(value)  # If there already is, call the insert function on that left child
        else:
            if self.right is None:  # Is there a right child?
                self.right = TreeNode(value, self)
            else:
                self.right.insert(value)  # If there already is, call the insert function on that right child.

    def delete(self, value):
        '''Delete a value from the tree.'''
        if not self:  # No tree given
            return None

        if self.value == value:  # The value to be deleted has been found
            # 4 Possibilities here...
            # 1. The node is a leaf and has no children
            if not self.left and not self.right:
                # Set whatever direction we went previously (L or R) to None
                return None
            
            # 2. The node has a right child
            elif not self.left and self.right:
                # Set the previous direction to Right
                return self.right
            
            # 3. The node has a left child
            elif not self.right and self.left:
                # Set the previous direction to Left
                return self.left
            
            # 4. The node has TWO children
            else:
                pointer = self.right  # Use a temp variable and go one to the right
                while pointer.left:
                    pointer = pointer.left  # Keep going left until you reach the smallest node

            # Swap the values of the pointer and the current node
            self.value = pointer.value
            self.right = self.right.delete(self.value)

        elif self.value > value:  
            self.left = self.left.delete(value)  # Keep searching to left
        else:
            self.right = self.right.delete(value)  # Keep searching to right

        # Return the node
        return self

    def inorder_traversal(self):
        '''Print out an ascending order In-order Traversal of the tree'''
        if self.left:  # If left child is not None
            self.left.inorder_traversal()  # Move down the left side of the tree
        print(self.value)  # Print the value at the middle node
        if self.right:  # If right child is not None
            self.right.inorder_traversal()  # Move down the right side of tree

    def preorder_traversal(self):
        '''Print out a Pre-order Traversal of the tree'''
        print(self.value)  # Print the value at the middle node
        if self.left:  # If left child is not None
            self.left.preorder_traversal()  # Move down the left side of the tree
        if self.right:  # If right child is not None
            self.right.preorder_traversal()  # Move down the right side of tree

    def postorder_traversal(self):
        '''Print out a Post-order Traversal of the tree'''
        if self.left:  # If left child is not None
            self.left.postorder_traversal()  # Move down the left side of the tree
        if self.right:  # If right child is not None
            self.right.postorder_traversal()  # Move down the right side of tree
        print(self.value)  # Print the value at the middle node

    def find(self, value):
        '''Return True if a value exists in the tree, False otherwise'''
        if value < self.value:
            if self.left is None:
                return False  # The value cannot exist in the tree
            else:
                return self.left.find(value)  # Otherwise, keep moving down the left side
        elif value > self.value:
            if self.right is None:
                return False  # The value cannot exist in the tree
            else:
                return self.right.find(value)  # Otherwise, keep moving down the right side
        else:
            return True  # The only last case is that the value equals the current node value

    def bfs(self):
        '''Return a Breadth-First Search of the tree'''
        if self is None:
            return None
        output = []  # Array to store return values
        queue = [self]  # Queue to store each tree node that we visit

        while queue:
            cur = queue.pop(0)  # start with root node
            output.append(cur.value)

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

        return output

    def subtree_first(self, value):
        '''Given a node in a BST, return the value that comes 
           first in traversal order within the subtree of node'''

        # Check if value is in tree
        if not self.find(value):
            return None

        # Traverse the tree to the node
        while self.value != value:
            if self.value > value:
                self = self.left
            else:
                self = self.right

        # Go to the left-most node
        while self.left:
            self = self.left

        return self.value

    def successor(self, value):
        '''Given a node in a BST, return the node that comes 
           NEXT in the tree's traversal order'''
        # Check if value is in tree
        if not self.find(value):
            return None
        
        # Traverse the tree to the node
        while self.value != value:
            if self.value > value:
                self = self.left
            else:
                self = self.right

        # Node has a right child
        if self.right:
            return self.subtree_first(self.right.value)  # Walk down to the leftmost node
        else:  # Node does not have a right child
            while self is not self.parent.left:  # Walk up tree until you go up a left branch
                self = self.parent
                if self.parent is None:  # There is no successor for the value
                    return None
            return self.parent.value  
    
    def find_parent(self, value):
        '''Test function to find parent node of a given value'''
        # Traverse through the tree to find the node
        while self.value != value:
            if self.value > value:
                self = self.left
            else:
                self = self.right
        return self.parent.value

    def get_min(self):
        '''Test function to find parent node of a given value'''
        # No Tree exists
        if not self:
            return None
        
        while self.left:
            self = self.left

        return self.value

    def get_max(self):
        '''Return the maximum value stored in the tree'''
        # No Tree exists
        if not self:
            return None
        
        while self.right:
            self = self.right

        return self.value

    def get_node_count(self):
        '''Return the number of nodes present in the tree'''
        #  The count of each node can be represented as such: 
        #  1 + the size of each of it's subtrees (left and right)
        if self.left and self.right:
            return 1 + self.left.get_node_count() + self.right.get_node_count()
        elif self.left:
            return 1 + self.left.get_node_count()
        elif self.right:
            return 1 + self.right.get_node_count()
        else:
            return 1
    
    def get_height(self):
        '''Return the height of the binary search tree'''
        #  Similar to the get_node_count function. Instead use a max() function
        #  to only count the height of the tallest subtree
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1

def main():
    # Create instance of tree
    tree = TreeNode(50)

    # Insert values into tree
    values = [20, 10, 30, 25, 35, 75, 100, 90]
    for value in values:
        tree.insert(value)

    # In-Order Traversal
    tree.inorder_traversal()

    # Pre-Order Traversal
    tree.preorder_traversal()

    # Post-Order Traversal
    tree.postorder_traversal()

    # Verify a value exists in tree
    print(tree.find(35))

    # BFS of tree
    print(tree.bfs())

    # Find smallest element in a node's subtree
    print(tree.subtree_first(30))

    # Find successor of node
    print(tree.successor(10))

    # Get parent of node
    print(tree.find_parent(20))

    # Get minimum value of tree
    print(tree.get_min())

    # Get maximum value of tree
    print(tree.get_max())

    # Get node count of tree
    print(tree.get_node_count())

    # Get height of tree
    print(tree.get_height())

    # Delete a node from tree
    tree.delete(30)
    print(tree.find(30))

if __name__ == '__main__':
    main()


