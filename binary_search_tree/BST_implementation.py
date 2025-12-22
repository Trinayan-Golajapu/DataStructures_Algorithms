class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data: # for duplicate values --> ignore
            return 
        if self.key > data: # for duplicate values --> place left side ---> self.key >= data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print('Node is  present')
            return
        elif self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('node is not present')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('node is not present')
    
    def preorder(self):
        if self.key is not None:
            print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()     
        if self.rchild:
            self.rchild.postorder()
        print(self.key)


root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
root.postorder()
# root.search(40)