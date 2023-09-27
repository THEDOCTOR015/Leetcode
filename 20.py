"""
Answer:
"""
class Solution:
    def isValid(self, s):
        stack = []
        brackets = {'(':')', '{':'}','[':']'}

        for c in s:
            if c in brackets: # detect opening bracket
                stack.append(c)
            elif stack and c == brackets[stack.pop()]: # detect closing bracket matching the last opening bracket
                continue
            else:
                return False
        
        return not stack # if stack is empty, all brackets were matched
        
"""
Tests:
"""
solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))