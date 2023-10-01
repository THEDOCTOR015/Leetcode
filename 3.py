"""
Answer:
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        caractused = set()
        beststring = ""
        candidatestring = ""
        for index in range(len(s)) :
            explorerindex = 0
            candidate = s[index]
            while candidate in caractused :
                if candidatestring[explorerindex] == candidate :
                    candidatestring = candidatestring[explorerindex+1:]
                    break
                caractused.remove(candidatestring[explorerindex])
                explorerindex +=1
            caractused.add(candidate)
            candidatestring += candidate
            if len(candidatestring) > len(beststring) :
                beststring = candidatestring
        return len(beststring)
        
"""
Tests:
"""
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))