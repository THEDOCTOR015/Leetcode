"""
Answer:
"""

class Solution:
    def groupAnagrams(self, strs):
        sortedstrs = []
        for element in strs :
          string = ""
          for char in sorted(element) :
             string += char
          sortedstrs.append(string)
        dictstrs = {}
        for index,element in enumerate(sortedstrs) :
          found = False
          for key in dictstrs :
            if key == element :
              dictstrs[element] += [strs[index]]
              found = True
          if not found :
            dictstrs[element] = [strs[index]]
        res = []
        for value in dictstrs.values() :
          res.append(value)
        
        return res

"""
Tests:
"""

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))