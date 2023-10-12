"""
Answer (2 pointeurs uncomplete):
"""
# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head):
        # Méthode magnifique !
        slow = head
        fast = head
        while True :
            if fast :
                fast = slow.next
                if fast :
                    fast = slow.next
            if slow :
                slow = slow.next
            if slow == fast :
                if slow :
                    return True
                return False

"""
Answer (terre brulée) :
""" 
class Solution:
    def hasCycle(self, head):
        head.val = 'X'
        head = head.next
        while head.val is not None :
            if head.val == 'X' :
                return True  
            head.val = 'X'
            head = head.next
        return False    
"""
Tests:
"""