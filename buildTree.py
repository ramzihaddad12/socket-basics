from node import * 
from tokenType import TokenType

# Class that build the tree of nodes from the tokens
class BuildTree: 
    def __init__(self, tokens):
        self.curr = 0 # pointer through the list of tokens
        self.tokens = tokens # the list of tokens 

    # Function that build the tree 
    def build(self):
        return self.expr()

    # Function that finds the +, - operations and creates a PlusingNode or MinusingNode accordingly 
    def expr(self):
        root = self.term()

        while self.curr < len(self.tokens) and self.tokens[self.curr].type in (TokenType.PLUS, TokenType.MINUS):
            if self.tokens[self.curr].type == TokenType.PLUS:
                self.curr += 1
                root = PlusingNode(root, self.term())
            elif self.tokens[self.curr].type == TokenType.MINUS:
                self.curr += 1
                root = MinusingNode(root, self.term())

        return root
    #  Function that finds the *, //, <<^ operations and creates a MultiplyingNode, DividingNode, ShiftingNode accordingly 
    def term(self):
        root = self.factor()

        while self.curr < len(self.tokens) and self.tokens[self.curr].type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.SHIFT):
            if self.tokens[self.curr].type == TokenType.MULTIPLY:
                self.curr += 1
                root = MultiplyingNode(root, self.factor())
            elif self.tokens[self.curr].type == TokenType.DIVIDE:
                self.curr += 1
                root = DividingNode(root, self.factor())
            elif self.tokens[self.curr].type == TokenType.SHIFT:
                self.curr += 1
                root = ShiftingNode(root, self.factor())
                
        return root

    #  Function that finds the lower level tokens (factors) and creates nodes accordingly 
    def factor(self):
        token = self.tokens[self.curr]

        if token.type == TokenType.NUM:
            self.curr += 1
            return ValueNode(token.val)

        elif token.type == TokenType.PLUS:
            self.curr += 1
            return PositiveNode(self.factor())
        
        elif token.type == TokenType.MINUS:
            self.curr += 1
            return NegativeNode(self.factor())

        elif token.type == TokenType.OBRACK:
            self.curr += 1
            root = self.expr()
            
            self.curr += 1
            return root