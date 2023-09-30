"""
Answer:
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def low(s):
            s = s.lower()
            s = "".join([i for i in s if i.isalnum()])
            return s
        s = low(s)
        if len(s) == 0:
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
"""
Tests:
"""
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome("aa"))
print(solution.isPalindrome(" ")) 
