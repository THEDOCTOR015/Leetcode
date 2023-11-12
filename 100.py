# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def explore(node1,node2):
        if node1 is None and node2 is None :
            return True
        if node1 is None or node2 is None :
            return False
        if node1.val != node2.val :
            return False
        resgauche = Solution.explore(node1.left,node2.left)
        resdroite = Solution.explore(node1.right,node2.right)
        if resgauche is False or resdroite is False :
            return False
        return True
    def isSameTree(self, p, q):
        if p is None and q is None :
            return True
        if p is None or q is None :
            return False
        return Solution.explore(p,q)