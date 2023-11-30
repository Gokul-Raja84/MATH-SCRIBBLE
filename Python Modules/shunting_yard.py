class ShuntingYard:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

    def shunting_yard(self, infix_expression):
        output = []
        operator_stack = []

        for token in infix_expression:
            if token.isalnum():
                output.append(token)
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] in self.operators and
                       ((self.associativity[token] == 'left' and self.operators[token] <= self.operators[operator_stack[-1]]) or
                        (self.associativity[token] == 'right' and self.operators[token] < self.operators[operator_stack[-1]]))):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Discard the '('

        while operator_stack:
            output.append(operator_stack.pop())

        return output

if __name__ == "__main__":
    shunting_yard_parser = ShuntingYard()

    # Example infix expression
    infix_expression = ['(', '3', '+', '5', ')', '*', '2', '^', '(', '4', '-', '2', ')']

    # Use the Shunting Yard Algorithm to convert infix to postfix
    postfix_expression = shunting_yard_parser.shunting_yard(infix_expression)
    print(f"Infix to Postfix: {' '.join(postfix_expression)}")
