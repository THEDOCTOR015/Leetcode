"""
Answer :
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root):
        if root == None: # Cas trivial
            return root
        root.left, root.right = root.right, root.left
        # Droite
        self.invertTree(root.right)
        # Gauche
        self.invertTree(root.left)
        return root