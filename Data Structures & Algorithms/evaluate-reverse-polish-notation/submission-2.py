class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackRes = []

        for item in tokens:
            if item == "+":
                a = int(stackRes.pop())
                b = int(stackRes.pop())
                stackRes.append(a + b)
            elif item == "-":
                a = int(stackRes.pop())
                b = int(stackRes.pop())
                stackRes.append(b - a)
            elif item == "*":
                a = int(stackRes.pop())
                b = int(stackRes.pop())
                stackRes.append(a*b)
            elif item == "/":
                a = int(stackRes.pop())
                b = int(stackRes.pop())
                stackRes.append(int(b/a)) #truncate to 0
            else:
                stackRes.append(int(item))
        return stackRes[0]
