"""
Answer:
"""
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        # Check obvious cases
        if len(t) > len(s) :
            return ""
        if t == s :
            return t
        bestguest = ""
        left = 0
        right = 0
        toggle = False
        tmap = Counter(t)
        havemap = {element:0 for element in alphabet}
        have = 0
        needmap = {element:0 for element in alphabet}
        for key,value in tmap.items() :
            needmap[key] = value
        need = len(tmap)
        while True :
            # Condition de sortie
            if right >= len(s) and have < need :
                break
            if toggle :
                # Si on supprime le caractère de gauche
                supcarac = s[left]
                havemap[supcarac] -= 1
                if havemap[supcarac] < needmap[supcarac]:
                    have -= 1
                left += 1
            else :
                # Si on ajoute le caractère de droite
                addcarac = s[right]
                havemap[addcarac] += 1
                if havemap[addcarac] == needmap[addcarac]:
                    have += 1
                right += 1
            if have == need :
                toggle = True
                if right - left < len(bestguest) or bestguest == "" :
                    bestguest = s[left:right]
            if have < need :
                toggle = False
        return bestguest


        
"""
Tests:
"""
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC")=="BANC")
print(solution.minWindow("a", "a")=="a")
print(solution.minWindow("aaaaa", "aa")=="aa")
print(solution.minWindow("a", "aa")=="")
