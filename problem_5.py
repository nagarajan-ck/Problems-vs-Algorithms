from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact



## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if(char not in current_node.children):
                current_node.children[char]=TrieNode()
            current_node = current_node.children[char]
        current_node.is_word=True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if(char not in current_node.children):
                return False
            current_node=current_node.children[char]
        return current_node




class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word=False
        self.children={}
        self.list_of_suffix=[]

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]=TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point


        current_node=self.children
        # print("suffix="+suffix)
        for word in suffix:
            current_node=current_node[word].children

        tries=current_node.keys()
        tries=list(tries) #['a','i']
        # print(suffix)
        # print(tries)
        if(len(tries)==0):

            return suffix


        for node in tries:
            # print(suffix)




            #print("suffix "+suffix)

            # print(self.list_of_suffix)
            # print(current_node[node].children,current_node[node].is_word)
            if(current_node[node].is_word):
                self.list_of_suffix.append(suffix+node)
            self.suffixes(suffix+node)
            # suffix=''



        # print(self.list_of_suffix)
        return self.list_of_suffix


def getSuffix(MyTrie,suffix):
    prefixNode = MyTrie.find(suffix)

    if(prefixNode):
        return prefixNode.suffixes()
    return prefixNode



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
        MyTrie.insert(word)


print(getSuffix(MyTrie,'f'))
print(getSuffix(MyTrie,'s'))
print(getSuffix(MyTrie,''))
