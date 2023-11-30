class ExpressionConverter:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

    def infix_to_postfix(self, infix_expression):
        output = []
        stack = []

        for token in infix_expression:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Discard the '('
            elif token in self.operators:
                while stack and stack[-1] in self.operators and (
                        (self.associativity[token] == 'left' and self.operators[token] <= self.operators[stack[-1]]) or
                        (self.associativity[token] == 'right' and self.operators[token] < self.operators[stack[-1]])):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def infix_to_prefix(self, infix_expression):
        infix_expression.reverse()
        for i in range(len(infix_expression)):
            if infix_expression[i] == '(':
                infix_expression[i] = ')'
            elif infix_expression[i] == ')':
                infix_expression[i] = '('

        postfix_expression = self.infix_to_postfix(infix_expression)
        postfix_expression.reverse()

        return postfix_expression

if __name__ == "__main__":
    converter = ExpressionConverter()

    # Example infix expression
    infix_expression = ['(', '3', '+', '5', ')', '*', '2', '^', '(', '4', '-', '2', ')']

    # Convert to postfix
    postfix_expression = converter.infix_to_postfix(infix_expression)
    print(f"Infix to Postfix: {' '.join(postfix_expression)}")

    # Convert to prefix
    prefix_expression = converter.infix_to_prefix(infix_expression)
    print(f"Infix to Prefix: {' '.join(prefix_expression)}")
