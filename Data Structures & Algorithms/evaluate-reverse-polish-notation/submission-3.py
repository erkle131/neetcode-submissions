class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if token is a number, push it onto the stack
        # if token is an operator, pop two elements off the stack
        # and perform the operation
        # push the result back onto the stack for the next operation

        stack = []

        for c in tokens:
            if c in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+': res = num1 + num2
                elif c == '-': res = num1 - num2
                elif c == '*': res = num1 * num2
                elif c == '/': res = int(num1 / num2)

                stack.append(res)
            else:
                stack.append(int(c))

        return stack[0]