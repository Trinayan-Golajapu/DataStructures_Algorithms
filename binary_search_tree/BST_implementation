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

root = BST(None)
list1 = [20,10,4,1,4,5,6]
for i in list1:
    root.insert(i)

root.search(4)