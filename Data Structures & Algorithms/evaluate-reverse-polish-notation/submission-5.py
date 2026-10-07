class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                op2 = stack.pop()
                op1 = stack.pop()

                result = 0
                match t:
                    case '+':
                        result = op1 + op2
                    case '-':
                        result = op1 - op2
                    case '*':
                        result = op1 * op2
                    case '/':
                        result = int(op1 / op2)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()