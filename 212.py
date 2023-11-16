class Solution:
    """
    Solution surement buggé
    """
    def findWords(self, board, words):
        self.words = words
        self.board = board
        self.res = []
        self.wordtree = {}
        self.m = len(board)
        self.n = len(board[0])
        # Etape 1 : on enregistre les mots dans notre arbre
        for word in words :
            word = word
            dictionary = self.wordtree
            for char in word :
                if not char in dictionary :
                    newdictionary = {}
                    dictionary[char] = newdictionary
                else :
                    newdictionary = dictionary[char]
                dictionary = newdictionary
        #print("normal:",self.wordtree)
        # Etape 2 : Vérifier si les mots sont dans l'arbre
        def removeword(word,tree):
            if word == "" :
                return
            char = word[0]
            if char not in tree :
                return
            posibility = tree[char].keys()
            if len(posibility) == 1 :
                if removeword(word[1:],tree[char]) is True:
                    tree[char] = {}
                    return True
            elif len(posibility) == 0 :
                return True
            elif len(posibility) >= 2 :
                for pos in posibility :
                    removeword(word[1:],tree[char][pos])
                return False
            
        def explore(x,y,banlist,word,dictionary) :
            #print((x,y),banlist,dictionary,word)
            if word in self.words and word not in self.res :
                removeword(word[1:],self.wordtree[word[0]])
                #print("word:",word)
                #print(self.wordtree)
                self.res.append(word)
            moves = [(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
            #print("moves:",moves)
            posmoves = []
            for move in moves :
                if move[0] < self.m and move[0] >= 0 and move[1] < self.n and move[1] >= 0 :
                    if move not in banlist :
                        posmoves.append(move)
            #print("posmoves:",posmoves)
            for move in posmoves :
                char = self.board[move[0]][move[1]]
                #print("char:",char)
                if char in dictionary :
                    newbanlist = banlist.copy() + [(x,y)]
                    explore(move[0],move[1],newbanlist,word+char,dictionary[char])
        # Etape 3 : Explorer chaque casse
        for i in range(self.m):
            for y in range(self.n) :
                char = self.board[i][y]
                if char in self.wordtree :
                    explore(i,y,[],char,self.wordtree[char])
        return self.res
                