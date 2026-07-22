class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a,b = stack.pop(), stack.pop()
                c = int(b-a)
                stack.append(c)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a,b = stack.pop(), stack.pop()
                d = int(b/a)
                stack.append(d)
            else :
                stack.append(int(i))
        return stack[0]