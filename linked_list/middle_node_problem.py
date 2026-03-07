class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        n = self.head
        while n is not None:
            print(n.data,'-->',end=' ')
            n = n.link
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node
            
    def middle_check(self,num,rule_num):
        n = self.head
        length_check = 0
        while n is not None:
            length_check = length_check + 1
            if length_check == num:
                if rule_num == 0:
                    return n.data
                else:
                    return n.data
                
                
            n = n.link
            
    def middle_node(self):
        length = 0
        temp = self.head
        while temp is not None:
            length = length + 1
            temp = temp.link
        
            
        num = (length // 2) + 1
        rule_num = num % 2
        # return rule_num
        
        a = self.middle_check(num,rule_num)
        return a
        
        

        
        
            
            
            
ll = LinkedList()
ll.add_begin(6)
ll.add_begin(5)
ll.add_begin(4)
ll.add_begin(3)
ll.add_begin(2)
ll.add_begin(1)

a = ll.middle_node()
print(a)

# ll.printLL()