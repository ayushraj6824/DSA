class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            print(f"Insert {data} at the beginning")
            
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        print(f"Insert {data} at the end")


    def display(self):
        if not self.head:
            print("Linked List is empty")
            return
        current=self.head
        while current:
            print(f"{current.data} ->",end="")
            current=current.next
        print("None")
    
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
        print("Linked List reversed")





# Linked List is a data structure where each element (node) points to the next one.
# It allows for efficient insertion and deletion of elements.   






# Example
linked_list=LinkedList()
linked_list.display()
linked_list.insert_at_end(8)
linked_list.insert_at_end(6)
linked_list.insert_at_end(7)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(7)
linked_list.insert_at_end(6)
linked_list.display()
linked_list.insert_at_end(5)
linked_list.display()   
linked_list.insert_at_end(4)
linked_list.display()
linked_list.reverse()
linked_list.display()