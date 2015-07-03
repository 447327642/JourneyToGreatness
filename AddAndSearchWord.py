END = '$'

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = {}
        
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[END] = {}
        return

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        if word == "":
            return END in node
        if word[0] == '.':
            for c in node:
                if self.find(node[c],word[1:]):
                    return True
        elif word[0] in node:
            return self.find(node[word[0]], word[1:])
        return False
            
                    

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

s = WordDictionary()

s.addWord("a")
s.addWord("a")

# print s.search(".") 
# print s.search("aa") 
# print s.search("a") 
print s.search(".a") 
print s.search("a.") 
