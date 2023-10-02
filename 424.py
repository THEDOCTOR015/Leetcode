"""
Answer:
"""
from collections import Counter
class Solution:
    def characterReplacement(self, s, k):
        def isvalid(string,k) :
            if len(string) <= 1 :
                return True
            mostcommon = Counter(string).most_common(1)
            if len(string) - (k + mostcommon[0][1]) <= 0:
                return True
            return False
        left = 0
        right = 0
        bestlenght = 0
        while right != len(s) :
            candidatstring = s[left:right+1]
            if isvalid(candidatstring,k) :
                bestlenght = max(bestlenght,len(candidatstring))
            else :
                left += 1
            right +=1
        return bestlenght


"""
Tests:
"""
solution = Solution()
print(solution.characterReplacement("ABAB",2)==4)
print(solution.characterReplacement("AABABBA",1)==4)
print(solution.characterReplacement("AABABBA",0)==2)
print(solution.characterReplacement("AABABBA",2)==5)
print(solution.characterReplacement("AABABBA",3)==7)
print(solution.characterReplacement("ABCDEF",4)==5)