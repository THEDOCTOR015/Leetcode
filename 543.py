class Solution:
    def __init__(self):
        self.diameter = 0  # Stocke le diametre maximum trouvé jusqu'à présent
    
    def depth(self, node) -> int:
        """
        Explorer les profondeur des 2 cotés
        """
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        """
        Calculer le diametre maximum possible a partir de ce node et le comparer au maximum trouvé pour le moment
        """
        if left + right > self.diameter:
            self.diameter = left + right
        # On renvoie la profondeur maximum trouvé
        return 1 + (left if left > right else right)


    
    def diameterOfBinaryTree(self, root) -> int:
        if not root: # Cas trivial
            return 0
        self.depth(root)
        return self.diameter