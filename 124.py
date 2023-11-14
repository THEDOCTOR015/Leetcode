# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def explore(self,rootnode) :
        if rootnode is None :
            return 0
        leftnode = rootnode.left if rootnode.left is not None else None
        rightnode = rootnode.right if rootnode.right is not None else None
        bestleft = self.explore(leftnode)
        bestright = self.explore(rightnode)
        # On calcule la meilleure route possible à partir de rootnode
        bestroad = max(bestleft+rootnode.val,bestright+rootnode.val,rootnode.val)
        # On essaie de dépaser max avec tout les élements
        bestmax = max(bestroad,bestleft+bestright+rootnode.val)
        if bestmax > self.max :
            self.max = bestmax
        return bestroad
        
    def maxPathSum(self, root):
        self.max = float("-inf")
        self.explore(root)
        return self.max