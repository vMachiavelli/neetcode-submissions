class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(i)
            else:
                num1 = int(stack[-1])
                stack = stack[:-1]
                num2 = int(stack[-1])

                if i == "+":
                    stack[-1] = num1 + num2
                if i == "*":
                    stack[-1] = num1 * num2
                if i == "-":
                    stack[-1] = num2 - num1
                if i == "/":
                    stack[-1] = num2 / num1

                print(stack[-1])
        return int(stack[-1])