# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution magnifique leetcode ( a refaire) 
"""
class Solution:
    def kthSmallest(self, root, k) -> int:
        stack, cur = [], root # first in, last out
        
        # iterative in-order DFS traversal
        while True:
            while cur: # go as left as possible
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # last one, smallest node
            k -= 1
            if k == 0:
                return cur.val
                
            cur = cur.right