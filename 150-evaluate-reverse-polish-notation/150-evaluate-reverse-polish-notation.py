class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","*","-","/"]:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if i == "+":
                    stack.append(val1+val2)
                elif i == "*":
                    stack.append(val1*val2)
                elif i=="-":
                    stack.append(val2-val1)
                else:
                    stack.append(int(val2/val1))
            else:
                stack.append(i)
        return stack[-1]
        