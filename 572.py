"""
Solution by leetcode car je voulai faire la meme
"""
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if subRoot == None :
            return True

        if root == None :
            return False

        if self.same(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

    def same(self , r , s):
        if r == None and s == None :
            return True

        if r and s and r.val == s.val:
            return self.same(r.right , s.right) and self.same(r.left , s.left)  

        return False