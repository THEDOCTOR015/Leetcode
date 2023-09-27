"""
Answer:
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
      self.stack.append(val)
        

    def pop(self) -> None:
      self.stack = self.stack[:len(self.stack)-1]
        

    def top(self) -> int:
      return self.stack[-1]
        

    def getMin(self) -> int:
      return min(self.stack)
      

"""
Tests:
"""

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2