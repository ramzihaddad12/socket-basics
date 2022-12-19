# Types of nodes needed to represented in the tree 

# Node representing a number value 
class ValueNode:
    def __init__(self, value):
        self.value = value

# Node representing a positive token ( a number starting with 1 or more + signs )
class PositiveNode:
    def __init__(self, node):
        self.node = node

# Node representing a negative token ( a number starting with 1 or more - signs )
class NegativeNode:
    def __init__(self, node):
        self.node = node

# Node representing a plusing operation
class PlusingNode: 
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2

# Node representing a minusing operation
class MinusingNode: 
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2

# Node representing a multiplying operation
class MultiplyingNode: 
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2

# Node representing a dividing operation
class DividingNode: 
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2

# Node representing a shifting operation
class ShiftingNode: 
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2