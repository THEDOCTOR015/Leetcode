# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Solution leetcode belle utilisation d'un deck
"""
from collections import deque
class Solution:
    def rightSideView(self, root):
        result = []
        q = deque([root])

        while q:
            rightMost = None
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMost:
                result.append(rightMost.val)
        return result
        