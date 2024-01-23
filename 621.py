"""
Answer (leetcode):
"""
from collections import Counter # Egalement Utilisable
class Solution:
    def leastInterval(self, tasks, n: int):
        cnts = [0] * 26
        for t in tasks:
            cnts[ord(t)-ord('A')] += 1
        max_occurence = max(cnts)
        max_occurence_cnt = cnts.count(max_occurence)
        len_full_fill = len(tasks) # Longueur minimum théorique (de la meilleure solution)
        len_part_fill = (max_occurence-1)*(n+1)+max_occurence_cnt # Longueur maximum théorique (de la meilleure solution)
        return max(len_full_fill, len_part_fill)
"""
Tests:
"""
solution = Solution()
print( solution.leastInterval(["A","A","A","B","B","B"], 0) )
print( solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) )
print( solution.leastInterval(["A","A","A","B","B","B"], 2) )
print( solution.leastInterval(["A","A","A","B","B","B","C"], 2))
print( solution.leastInterval(["A","A","A","B","B","B","C","C"], 2))
print( solution.leastInterval(["A","B","C","D","E","F","G","H"], 2))

