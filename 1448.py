# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) :
        self.compteur = 0
        
    def explore(self,node,maximum) :
        if node.val >= maximum :
            self.compteur += 1
        newmax = max(maximum,node.val)
        Solution.explore(self,node.left,newmax) if node.left is not None else None
        Solution.explore(self,node.right,newmax) if node.right is not None else None

    def goodNodes(self, root) -> int:
        Solution.explore(self,root,root.val)
        return self.compteur