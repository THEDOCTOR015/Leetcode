# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) :
        self.compteur = 0

    def explore(self,node,number) :
        if number > self.compteur :
            self.compteur = number
        if node is None :
            return node
        Solution.explore(self,node.left,number+1)
        Solution.explore(self,node.right,number+1)

    def maxDepth(self, root):
        Solution.explore(self,root,0)
        return self.compteur