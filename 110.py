# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def explore(node,number) :
        depthleft = Solution.explore(node.left,number+1) if node.left is not None else number
        depthright = Solution.explore(node.right,number+1) if node.right is not None else number
        if depthleft is False or depthright is False :
            return False
        if abs(depthleft-depthright) >= 2 :
            return False
        return max(depthleft,depthright)
    def isBalanced(self, root):
        if root is None :
            return True
        if root.left is None and root.right is None :
            return True
        return Solution.explore(root,0)