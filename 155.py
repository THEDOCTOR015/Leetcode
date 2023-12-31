"""
Answer:
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
      self.stack.append(val)
      if self.minstack == [] :
        self.minstack.append(val)
      else :
        actualminimum = self.minstack[-1]
        if val < actualminimum :
          self.minstack.append(val)
        else :
          self.minstack.append(actualminimum)
        

    def pop(self) -> None:
      self.stack = self.stack[:len(self.stack)-1]
      self.minstack = self.minstack[:len(self.minstack)-1]
        

    def top(self) -> int:
      return self.stack[-1]
        

    def getMin(self) -> int:
      return self.minstack[-1]
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