# A RouteTrie will store our routes and their associated handlers
class RouteTrie: #THE ENTIRE TRIE
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, url,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        urlArr = url.split('/')
        current_node = self.children
        for i in urlArr:
            if(i not in current_node.children):
                current_node.children[i]=RouteTrieNode()
            current_node = current_node.children[i]
        current_node.handler = handler

    def find(self, url):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        urlArr = url.split('/')
        current_node = self.root
        for i in urlArr:
            if(i not in current_node.children):
                return None
            current_node = current_node.children[i]
        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode: #EACH INDIVIDUAL NODE
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children={}
        self.handler=None

    def insert(self, endpoint):
        # Insert the node as before
        self.children[endpoint] = RouteTrieNode()
