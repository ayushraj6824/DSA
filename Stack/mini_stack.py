class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if not self.stack:
            return None
        return min(self.stack)
    


# Example usage:
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(8)
    print(min_stack.getMin())  # Output: 2
    print(min_stack.top())      # Output: 8
    min_stack.pop()
    print(min_stack.getMin())  # Output: 2