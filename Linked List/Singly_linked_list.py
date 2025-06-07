class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,item):
        new_node=Node(item,self.start)
        self.start=new_node 
    def insert_at_end(self,item):
        new_node=Node(item)
        if self.is_empty():
            self.start=new_node
            return
        current=self.start
        while current.next:
            current=current.next
        current.next=new_node   
    