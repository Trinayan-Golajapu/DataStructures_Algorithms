class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->', end='')
                n = n.nref
    
    def backward_traversal(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            
            while n is not None:
                print(n.data,'-->', end='')
                n = n.pref
    
    def insert_empty(self,data):
        new_node = Node(data)
        self.head = new_node
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            print('Linked List is Empty')
            return
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        while self.head is None:
            print('Linked List is Empty')
            return
        n = self.head
        while n.nref is not None:
            n = n.nref

        new_node.pref = n
        n.nref = new_node


    def add_after(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print(f'{x} node is not there in Linked List')
            else:
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:

                    n.nref.pref = new_node
                n.nref = new_node
    
    def add_before(self,data,x):
        new_node = Node(data)
        if self.head is None:
            print('LL is Empty')
        else:
            n = self.head

            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print(f'{x} node is not there in LL')
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:

                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.nref is None:
            self.head = None
        else:
            n = self.head
            self.head = n.nref
            self.head.pref = None
    
    def delete_end(self):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.pref is None and self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref = None
    
    def delete_value(self, x):
        if self.head is None:
            print('LL is empty')
            return
        if self.head.nref is None and self.head.data == x:
            self.head = None
            return
        
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return 
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref  = n.nref
            n.nref.pref = n.pref

        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print('given node is not present in LL')

            



    
        
        




LL = LinkedList()
LL.insert_empty(10)
LL.add_begin(5)
LL.add_end(15)
LL.add_after(3,10)
LL.add_after(22,15)
LL.add_before(99,3)
LL.add_before(550,5)
LL.delete_begin()
LL.delete_end()
LL.delete_value(99)
LL.forward_traversal()

# LL.backward_traversal()