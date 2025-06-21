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
    def delete_at_start(self):
        if self.is_empty():
            return
        self.start=self.start.next          
    def delete_at_end(self):            
        if self.is_empty():
            return
        if self.start.next==None:
            self.start=None
            return
        current=self.start
        while current.next.next:
            current=current.next
        current.next=None
    def display(self):  
        if self.is_empty():
            print("List is empty")
            return
        current=self.start
        while current:
            print(current.item,end=" -> ")
            current=current.next
        print("None")   



    def search(self,item):

        if self.is_empty():
            return False
        current=self.start
        while current:
            if current.item==item:
                return True
            current=current.next
        return False    


    def delete_item(self,item):
        if self.is_empty():
            return
        if self.start.item==item:
            self.start=self.start.next
            return
        current=self.start
        while current.next:
            if current.next.item==item:
                current.next=current.next.next
                return
            current=current.next
        print("Item not found") 
            
            
   