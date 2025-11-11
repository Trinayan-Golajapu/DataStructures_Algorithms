class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print('Linked List is Empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'--->', end=' ')
                n = n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: 
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def insert_after(self,data,x):
        new_node = Node(data)
        n = self.head
        while n.data != x:
            n = n.ref

        a = n.ref
        n.ref = new_node
        new_node.ref = a

    def insert_before(self,data,x):
        new_node = Node(data)
        
        n = self.head

        if n.data == x:
            new_node.ref = n
            self.head = new_node
            return

        while n.ref.data != x:
            n = n.ref
            if n.ref is None:
                print('Node not found')
                return
        
        a = n.ref
        n.ref = new_node
        new_node.ref = a
    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked List is not Empty')
    
    def delete_begin(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            n = self.head
            self.head = n.ref
    
    def delete_end(self):
        if self.head is None:
            print('linked List is Empty')
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def delete_by_value(self,x):
        if self.head is None:
            print('Linked List is Empty')
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        try:

            n = self.head
            while n.ref.data != x:
                n = n.ref

            a = n.ref.ref
            n.ref = a
        except:
            print('given data node is not present')







LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.add_end(200)
LL1.insert_after(39,100)
LL1.insert_after(49,39)
LL1.insert_before(999,100)
LL1.insert_before(888,200)
LL1.insert_before(777,20)
LL1.insert_after(599,39)
LL1.insert_before(555,666)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(100)
LL1.delete_by_value(49)
LL1.delete_by_value(888)
LL1.delete_by_value(8)
LL1.print_LL()