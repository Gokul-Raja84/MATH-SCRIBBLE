class OperatorPrecedenceParser:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

    def parse_expression(self, expression):
        tokens = self.tokenize(expression)
        postfix_expression = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix_expression)
        return result

    def tokenize(self, expression):
        # Split the expression into tokens (numbers, operators, parentheses)
        # For simplicity, assumes that the expression is space-separated
        return expression.split()

    def infix_to_postfix(self, tokens):
        output = []
        stack = []

        for token in tokens:
            if token.isnumeric():
                output.append(token)
            elif token in self.operators:
                while stack and stack[-1] in self.operators and (
                        (self.associativity[token] == 'left' and self.operators[token] <= self.operators[stack[-1]]) or
                        (self.associativity[token] == 'right' and self.operators[token] < self.operators[stack[-1]])):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Discard the '('

        while stack:
            output.append(stack.pop())

        return output

    def evaluate_postfix(self, postfix_expression):
        stack = []

        for token in postfix_expression:
            if token.isnumeric():
                stack.append(float(token))
            elif token in self.operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.perform_operation(operand1, operand2, token)
                stack.append(result)

        return stack[0] if stack else None

    def perform_operation(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '^':
            return operand1 ** operand2

if __name__ == "__main__":
    parser = OperatorPrecedenceParser()
    expression = "3 + 5 * ( 2 - 8 ) / 4"
    result = parser.parse_expression(expression)
    print(f"Result of '{expression}': {result}")