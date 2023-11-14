class Solution:
    def findDuplicate(self, nums) -> int:
        """
        Solution magnifique Floyd
        """ 
        slow = nums[0]
        fast = nums[0]
        # On fait déplacer les pointeurs une première fois
        slow = nums[slow]
        fast = nums[nums[fast]]
        # On boucle tant que les 2 pointeur ne sont pas rejoint
        while slow != fast :
            slow = nums[slow]
            fast = nums[nums[fast]]
        # On remet le pointeur slow au début
        slow = nums[0]
        while slow != fast :
            slow = nums[slow]
            fast = nums[fast]
        # Lorsque les pointeur sont rejoint a nouveau, on a trouvé le debut du cycle (car il y a 2 ou plus objet qui pointe vers le meme nombre aka le duplica)
        return slow