"""
Answer (not complete):
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        #Etape 1 : Isoler en 2 linked listes
        slow = head
        fast = head.next
        while True :
            if fast == None or fast.next == None :
                break
            slow = slow.next
            fast = fast.next.next
        
        #Etape 2 : Inverser la 2eme deuxième liste
        liste2 = slow.next
        slow.next = None
        print(liste2.val)
        liste2rev = ListNode(liste2.val)
        while True :
            liste2 = liste2.next
            if liste2 is None :
                break
            liste2rev = ListNode(liste2.val,liste2rev) 
        
        #Etape 3 : Merger les 2 linked listes
        while True :
            tmp1, tmp2 = head.next , liste2rev.next
            head.next = liste2rev.val
            tmp1 = tmp1.next
            liste2rev = tmp2
            
        return head
            
            
            
"""
Answer (neetcode) :
"""      
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head        

"""
Answer (usable) :
"""
class Solution:
    def reorderList(self, head):
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next

        n = len(nodes)
        half  = n // 2
        i = 0
        while i < half:
            temp = nodes[i].next
            nodes[i].next = nodes[-i - 1]
            nodes[-i - 1].next = temp
            i += 1
        nodes[half].next = None
        return head
"""
Tests:
"""
solution = Solution()
head1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
test1 = solution.reorderList(head1)
while True :
    print(test1.val)
    test1 = test1.next
    if test1 is None :
        break
