"""
Answer:
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = ["+","-","*","/"]
        for element in tokens :
            if element in operators :
                print("stack : ",stack)
                n1 = stack.pop()
                n2 = stack.pop()
                nresult = eval(n2+element+n1)
                stack.append(str(int(nresult)))
            else :
                print("stack : ",stack)
                stack.append(element)
        return int(stack[0])       

"""
Tests:
"""
solution = Solution()
print(solution.evalRPN(["2","1","+","3","*"])) # 9
print(solution.evalRPN(["4","13","5","/","+"])) # 6