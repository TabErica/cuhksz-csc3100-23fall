
def closest_adj_price(prices):
    min_diff = abs(prices[0] - prices[1])
    for i in range(len(prices) - 1):
        diff = abs(prices[i] - prices[i + 1])
        min_diff = min(min_diff, diff)
    return min_diff


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value <= node.value:
            if node.left is None:
                new_node = TreeNode(value)
                new_node.parent = node
                node.left = new_node
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                new_node = TreeNode(value)
                new_node.parent = node
                node.right = new_node
            else:
                self._insert(node.right, value)
                
    def find_successor(self, value):
        node = self._find_node(self.root, value)
        if node is None:
            return None

        # If the right subtree is not empty, the successor is the leftmost
        # node in the right subtree.
        if node.right is not None:
            return self._find_min(node.right)

        # Otherwise, climb up the tree to find the first ancestor whose left
        # child is also an ancestor of the given node.
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent

        return parent

    def find_predecessor(self, value):
        node = self._find_node(self.root, value)
        if node is None:
            return None

        if node.left is not None:
            return self._find_max(node.left)

        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent

        return parent

    def _find_node(self, node, value):
        # Helper function to find a node with the given value in the BST.
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)

    def _find_min(self, node):
        # Helper function to find the node with the minimum value in a subtree.
        while node.left is not None:
            node = node.left
        return node

    def _find_max(self, node):
        # Helper function to find the node with the maximum value in a subtree.
        while node.right is not None:
            node = node.right
        return node

def closest_price(prices):
    closest = float('inf')
    global bst
    bst = BST()
    for value in prices:
        bst.insert(value)
        
    current_node = bst.root
    stack = []
    prev_value = None
    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        if prev_value is not None:
            diff = abs(current_node.value - prev_value)
            closest = min(closest, diff)
        prev_value = current_node.value
        current_node = current_node.right

    return closest
    
def perform_operations(n, m, initial_sequence, operations):
    #prices = initial_sequence.copy()
    CLOSEST_ADJ = closest_adj_price(initial_sequence)
    CLOSEST_PRICE = closest_price(initial_sequence)
    
    for operation in operations:
        if operation[0] == 'BUY':
            x = int(operation[1])
            
            initial_sequence.append(x)
            new = abs(x - initial_sequence[-2])
            CLOSEST_ADJ = min (CLOSEST_ADJ, new)
            
            bst.insert(x)
            if bst.find_successor(x) != None and bst.find_predecessor(x) != None:
                new1 = abs(x - bst.find_successor(x).value)
                new2 = abs(bst.find_predecessor(x).value - x)
                CLOSEST_PRICE = min (CLOSEST_PRICE, new1, new2)
            elif bst.find_successor(x) == None and bst.find_predecessor(x) != None:
                new2 = abs(bst.find_predecessor(x).value - x)
                CLOSEST_PRICE = min (CLOSEST_PRICE, new2)
            elif bst.find_successor(x) != None and bst.find_predecessor(x) == None:
                new1 = abs(x - bst.find_successor(x).value)
                CLOSEST_PRICE = min (CLOSEST_PRICE, new1)
        elif operation[0] == 'CLOSEST_ADJ_PRICE':
            print(CLOSEST_ADJ)
        elif operation[0] == 'CLOSEST_PRICE':
            print(CLOSEST_PRICE)

if __name__ == "__main__":
    n, m = map(int, input().split())
    initial_sequence = list(map(int, input().split()))

    operations = []
    for _ in range(m):
        operations.append(input().split())

    perform_operations(n, m, initial_sequence, operations)