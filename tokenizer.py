from token import Token
from tokenType import TokenType

# Class that tokenizes the expression
class Tokenizer: 
    def __init__(self, expr):
        self.curr = 0 # pointer through the expression 
        self.expr = expr # expression to be tokenized 

    # Function that gets the number value for a certain token 
    def get_number(self):
        number = self.expr[self.curr]
        self.curr += 1
        num_of_decimals = 0

        # while the character read is a number or decimal 
        while  self.curr < len(self.expr) and (self.expr[self.curr] in '1234567890' or self.expr[self.curr] == '.'):
            # if more than 1 decimal points found --> end of number 
            if num_of_decimals > 1:
                break

            if self.expr[self.curr] == '.':
                num_of_decimals += 1
            # append to number if character is a number or first decimal 
            number += self.expr[self.curr]
            self.curr += 1
        #r return number token 
        return Token(TokenType.NUM, int(number))

    # Function that gets all the tokens for an expression 
    def get_all_tokens(self):
        tokens = []
        # while iterating over the expression 
        while self.curr < len(self.expr):
            # if + symbol found, token is of type PLUS 
            if self.expr[self.curr] == '+':
                tokens.append(Token(TokenType.PLUS, None))
                self.curr += 1
            # if - symbol found, token is of type MINUS 
            elif self.expr[self.curr] == '-':
                tokens.append(Token(TokenType.MINUS, None))
                self.curr += 1
            # if * symbol found, token is of type MULTIPLY 
            elif self.expr[self.curr] == '*':
                tokens.append(Token(TokenType.MULTIPLY, None))
                self.curr += 1
            # if ( symbol found, token is of type OBRACK 
            elif self.expr[self.curr] == '(':
                tokens.append(Token(TokenType.OBRACK, None))
                self.curr += 1
            # if ) symbol found, token is of type EBRACK 
            elif self.expr[self.curr] == ')':
                tokens.append(Token(TokenType.EBRACK, None))
                self.curr += 1
            # if // symbol found, token is of type DIVIDE 
            elif self.expr[self.curr] == '/' and self.expr[self.curr + 1] == '/':
                tokens.append(Token(TokenType.DIVIDE, None))
                self.curr += 2
            # if <<^ symbol found, token is of type SHIFT 
            elif self.expr[self.curr] == '<' and self.expr[self.curr + 1] == '<' and self.expr[self.curr + 2] == '^':
                tokens.append(Token(TokenType.SHIFT, None))
                self.curr += 3
            # if digit or decimal point is found, get whole number and token is of type NUM 
            elif self.expr[self.curr] in '1234567890' or self.expr[self.curr] == '.':
                tokens.append(self.get_number())
            # if \t or \n symbol found, we can ignore
            elif self.expr[self.curr] in ' \t\n':
                self.curr += 1
        # return all tokens 
        return tokens