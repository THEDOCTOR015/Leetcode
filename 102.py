# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) :
        self.candidate = []
        self.newcandidate = []
        self.output = []
    def explore(self) :
        """
        Parcoure chacun des candidat pour les ajouter a l'output et alimente la liste de nouveau candidats
        """
        outputnodes = []
        if self.candidate == [] :
            return
        for node in self.candidate :
            if node is None :
                continue
            outputnodes.append(node.val)
            self.newcandidate.append(node.left) if node.left is not None else None
            self.newcandidate.append(node.right) if node.right is not None else None
        print(outputnodes)
        self.output.append(outputnodes)
        self.candidate = self.newcandidate.copy()
        self.newcandidate = []
        Solution.explore(self)
            
    def levelOrder(self, root):
        if root is None :
            return []
        self.candidate = [root]
        Solution.explore(self)
        return self.output
        