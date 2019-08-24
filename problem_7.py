class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()


    def insert(self, urlArr,handler):
        current_node = self.root
        for i in urlArr:
            if(i not in current_node.children):
                current_node.children[i]=RouteTrieNode()
            current_node = current_node.children[i]

        current_node.handler = handler


    def find(self, urlArr):
        current_node = self.root
        for i in urlArr:
            if(i not in current_node.children):
                return 'not found handler'
            current_node = current_node.children[i]

        return current_node.handler



class RouteTrieNode:
    def __init__(self):
        self.children={}
        self.handler='not found handler'


    def insert(self, endpoint):
        self.children[endpoint] = RouteTrieNode()



class Router:
    def __init__(self,handler):
        self.route = RouteTrie()
        self.route.insert('/',handler)


    def add_handler(self, path, handler):
        if(path.endswith('/')):
            urlArr=self.split_path(path[:-1])
        else:
            urlArr=self.split_path(path)
        self.route.insert(urlArr,handler)


    def lookup(self, path):
        if(path.endswith('/')):
            urlArr=self.split_path(path[:-1])
        else:
            urlArr=self.split_path(path)
        return self.route.find(urlArr)


    def split_path(self, path):
        urlArr= path.split('/')
        urlArr[0]='/'
        return urlArr




router=Router("root handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/info/", "info handler")

print(router.lookup("/")) # prints 'root handler'

print(router.lookup("/home")) # prints 'not found handler' since it is not handled

print(router.lookup("/home/about")) # prints 'about handler' without trailing slash

print(router.lookup("/home/about/")) # prints 'about handler' with trailing slash

print(router.lookup("/home/info"))  # prints 'info handler'
