from enum import Enum

# Types of tokens available
class TokenType(Enum):
    PLUS = 0 # Plus operation (+)
    MINUS = 1 # Minus operation (-)
    DIVIDE = 2 # Divide operation (//)
    MULTIPLY = 3 # Multiply operation (*)
    SHIFT = 4 # Shift operation (<<^)
    OBRACK = 5 # Opening bracket 
    EBRACK = 6 # ending bracket 
    NUM = 7 # Number

