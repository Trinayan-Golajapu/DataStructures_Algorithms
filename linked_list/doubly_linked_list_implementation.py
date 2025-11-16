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




    
        
        




LL = LinkedList()
LL.insert_empty(10)
LL.add_begin(5)
LL.add_end(15)
LL.add_after(3,10)
LL.add_after(22,15)
LL.add_before(99,3)
LL.add_before(550,5)
LL.forward_traversal()
# LL.backward_traversal()