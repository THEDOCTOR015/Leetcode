class WordDictionary:
    """
    Super utile les dictionnaire dans les dictionnaire pour les trie (# pour signifier un fin de mot)
    """
    def __init__(self):
        self.worddict = {}

    def addWord(self, word: str) -> None:
        def insert(word,dictionary) :
            if word == "" :
                return
            char = word[0]
            if not char in dictionary.keys() :
                newdictionary = {}
                dictionary[char] = newdictionary
            else :
                newdictionary = dictionary[char]
            insert(word[1:],newdictionary)
        insert(word+"#",self.worddict)
            
    def search(self, word: str) -> bool:
        def find(word,dictionary) :
            if word == "" :
                return True
            char = word[0]
            if char == "." :
                for element in dictionary.keys() :
                    if find(word[1:],dictionary[element]) :
                        return True
                return False
            elif char in dictionary :
                return find(word[1:],dictionary[char])
            else :
                return False
        res = find(word+"#",self.worddict)
        return res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)