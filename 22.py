"""
Answer :
"""
global listparenthesis
listparenthesis = []
class Solution:
    def checkparenthesis(parenthesis,goal) :
        left = 0
        right = 0
        for element in parenthesis :
            if right > left :
                return False
            if element == "(" :
                left +=1
            else :
                right +=1
        if right == goal and left == goal :
            listparenthesis.append(parenthesis)
            return True
        elif right > goal or left > goal :
            return False
        return None

    def explore(currentparenthesis,goal) :
        if Solution.checkparenthesis(currentparenthesis,goal) != None :
            return
        newparenthesisleft = currentparenthesis + "("
        newparenthesisright = currentparenthesis + ")"
        Solution.explore(newparenthesisleft,goal)
        Solution.explore(newparenthesisright,goal)

        
    def generateParenthesis(self, n: int):
        Solution.explore("(",n)
        return listparenthesis
        
"""
Tests :
"""
solution = Solution()
print(solution.generateParenthesis(8))