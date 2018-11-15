from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class BinaryTree(object):
    
    # Constructor takes no additional arguments
    def __init__(self): 
        self.val = None
        self.left = None
        self.right = None
    
    # This method will insert val into the tree
    def insert(self, val): 
        # If the binary tree hasn't already been populated yet
        if self.val == None:
            self.val = val
        # when value is less than current node value, and left subtree is not yet a BT
        elif val < self.val and self.left == None:
            leftTree = BinaryTree()
            leftTree.val = val
            self.left = leftTree
        # when value is less than current node value, and left subtree is a BT
        elif val < self.val and self.left != None:
            self.left.insert(val)
        # when value is greater than current node value, and right subtree is not yet a BT
        elif val > self.val and self.right == None:
            rightTree = BinaryTree()
            rightTree.val = val
            self.right = rightTree
        # when value is greater than current node value, and right subtree is a BT
        elif val > self.val and self.right != None:
            self.right.insert(val)
        
    def remove(self, val):
        # node doesn't exist
        if not self:
            return self
        # search/remove from left if value at root of tree is greater than desired value
        if self.val > val:
            self.left = BinaryTree.remove(self.left, val)
        # search/remove from right if value at root of tree is less than desired value
        elif self.val < val:
            self.right = BinaryTree.remove(self.right, val)
        # remove from tree if value at root of tree is equal to desired value
        else:
            # replace with subtree if there exists only 1 of them
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            
            # case when there are two subtrees -- set head to max value from left subtree
            # and then delete node with max value in left subtree
            temp = self.left
            maxi = temp.val
            while temp.right:
                temp = temp.right
                maxi = temp.val
            self.val = maxi
            self.left = BinaryTree.remove(self.left, self.val)
        return self
            
    # helper function to go down tree from left to right in 'DFS' manner
    def helper(self, depth, nodes):
        # appends the node to the list of nodes at the level
        if depth == 0:
            nodes.append(self.val)
        else:
            # if left subtree exists, keep going down the left level to get to desired depth
            if self.left:
                nodes = self.left.helper(depth - 1, nodes)
            else:
                # nodes do not exist at left subtree
                nodes.extend([None] * (2 ** (depth-1)))
            
            # if right subtree exists, keep going down the right level to get to desired depth
            if self.right:
                nodes = self.right.helper(depth - 1, nodes)
            else:
                # nodes do not exist at right subtree
                nodes.extend([None] * (2 ** (depth-1)))
        return nodes
    
    # Calls upon helper function to get list of values at desired level from left to right
    def getValues(self, depth):
        return self.helper(depth, [])

class DFSTraversal():
    def __init__(self, tree, traversalType):
        # original tree
        self.bt = tree
        # list of values to be populated according to traversal type
        self.nodes = []
        self.changeTraversalType(traversalType)

        # index for iter
        self.index = 0

    def changeTraversalType(self, traversalType):
        # empty out list of nodes to populate nodes in diff order
        self.nodes = []
        self.index = 0

        # checking which traversal type to do
        if traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(self.bt)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(self.bt)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.inorder(self.bt)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        # fails when index falls out of list range
        try:
            node = self.nodes[self.index] 
        except IndexError:
            raise StopIteration() 
        # raise index when successful
        self.index += 1
        return node

    # inorder traversal - display Left, Node, Right
    def inorder(self, bt):
        if bt != None:
            self.inorder(bt.left)
            self.nodes.append(bt.val)
            self.inorder(bt.right)

    # preorder traversal - display Node, Left, Right
    def preorder(self, bt):
        if bt != None:
            self.nodes.append(bt.val)
            self.preorder(bt.left)
            self.preorder(bt.right)

    # postorder traversal - display Left, Right, Node
    def postorder(self, bt):
        if bt != None:
            self.postorder(bt.left)
            self.postorder(bt.right)
            self.nodes.append(bt.val)