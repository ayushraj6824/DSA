class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")

    def reverse(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp_stack.push(self.pop())
        self.item = temp_stack.item


s1 = Stack()
s1.push(110)
s1.push(204)
s1.push(300)
# s1.pop()
print("Original stack:", s1.item)


s1.reverse()
print("Reversed stack:", s1.item)

