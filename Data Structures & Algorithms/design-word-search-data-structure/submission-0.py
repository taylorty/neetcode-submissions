class TrieNode():
  
  # Initialize TrieNode instance
  def __init__(self):
    # Empty list of child nodes
    self.children = []
    # False indicates this node is not the end of a word
    self.complete = False
    # Create 26 child nodes for each letter of alphabet
    for i in range(0, 26):
      self.children.append(None)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            node = curr.children[ord(char) - ord('a')]
            if not node:
                curr.children[ord(char) - ord('a')] = TrieNode()
                node = curr.children[ord(char) - ord('a')]
                
            curr = node
        curr.complete = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word, i, node):
        if not node:
            return False
        if len(word) == i:
            if node.complete:
                return True
            return False
        index = ord(word[i]) - ord('a')
        if word[i] == '.':
            for j in range(26):
                if self.search_helper(word, i + 1, node.children[j]):
                    return True

            return False
        return self.search_helper(word, i + 1, node.children[index])
