class Node:
    def __init__(self,value)->None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self)->None:
        self.root = None

    def insert(self,value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if temp.value == value:return False
            if temp.value >value:
                if temp.left == None:
                    temp.left = newNode
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = newNode
                    return True
                else:
                    temp = temp.right

    def BFS(self):
        self.queue = []
        self.result = []
        self.queue.append(self.root)
        while len(self.queue)>0:
            self.result.append(self.queue[0].value)
            if self.queue[0].left != None:
               self.queue.append(self.queue[0].left)
            if self.queue[0].right != None:   
               self.queue.append(self.queue[0].right)
            self.queue.pop(0)
        return self.result


    def DFS_preorder(self):
        self.results = []
        def traverse(current_node):
            self.results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return self.results


    def DFS_postorder(self):
        self.postresults = []
        def post_traverse(current_node)->None:
            if current_node.left is not None:
                post_traverse(current_node.left)
            if current_node.right is not None:
                post_traverse(current_node.right)
            self.postresults.append(current_node.value)
        post_traverse(self.root)
        return self.postresults


    def DFS_inorder(self):
        self.inorderresults = []
        def inorder_intraverse(current_node):
            if current_node.left is not None:
                inorder_intraverse(current_node.left)
            self.inorderresults.append(current_node.value)
            if current_node.right is not None:
                inorder_intraverse(current_node.right)
        inorder_intraverse(self.root)
        return self.inorderresults                                                        


my_bst = BinarySearchTree()
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)
print(my_bst.BFS())
print(my_bst.DFS_preorder())
print(my_bst.DFS_postorder())
print(my_bst.DFS_inorder())
