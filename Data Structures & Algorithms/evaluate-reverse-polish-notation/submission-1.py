class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpnStack = []
        
        for i in range(0, len(tokens)):
            if tokens[i] == '+':
                b = int(rpnStack.pop())
                a = int(rpnStack.pop())
                rpnStack.append(a + b)     
            elif tokens[i] == '-':
                b = int(rpnStack.pop())
                a = int(rpnStack.pop())
                rpnStack.append(a - b)  
            elif tokens[i] == '*':
                b = int(rpnStack.pop())
                a = int(rpnStack.pop())
                rpnStack.append(a * b)   
            elif tokens[i] == '/':
                b = int(rpnStack.pop())
                a = int(rpnStack.pop())
                rpnStack.append(a / b)
            else:
                rpnStack.append(tokens[i])


        return int(rpnStack[0])