from node import *

# A class that calculates the final value result of the tree 
class Calculator:
    # Function that calculates the final value
    def calculate(self, node):
        # if the type of node is value node, then the value of the node is returned
        if type(node) is ValueNode:
            return node.value
        # if the type of node is negative node, then the operation is performed
        elif type(node) is NegativeNode:
            return -self.calculate(node.node)
        # if the type of node is positive node, then the operation is performed
        elif type(node) is PositiveNode:
            return self.calculate(node.node)
        # if the type of node is plusing node, then the operation is performed
        elif type(node) is PlusingNode:
            return self.calculate(node.node_1) + self.calculate(node.node_2)
        # if the type of node is minusing node, then the operation is performed
        elif type(node) is MinusingNode:
            return self.calculate(node.node_1) - self.calculate(node.node_2)
        # if the type of node is multiplying node, then the operation is performed
        elif type(node) is MultiplyingNode:
            return self.calculate(node.node_1) * self.calculate(node.node_2)
        # if the type of node is shifting node, then the operation is performed       
        elif type(node) is ShiftingNode:
            return (int(self.calculate(node.node_1)) << 13) ^  int(self.calculate(node.node_2))
        # if the type of node is dividing node, then the operation is performed
        elif type(node) is DividingNode:
            return self.calculate(node.node_1) // self.calculate(node.node_2)