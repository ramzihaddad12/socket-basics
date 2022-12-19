from tokenType import TokenType

# Class that represents a token
class Token:
    def __init__(self, type, val):
        self.type = type # type of token
        self.val = val # value of token (if NUM)