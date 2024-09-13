class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def delete(self, element):
        try:
            i = self.heap.index(element)
            
            self.heap[i] = self.heap[-1]
            self.heap.pop()
        
            self._heapify_down(i)
            self._heapify_up(i)
        except ValueError:
            print("Element not found in the heap.")

    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def print_heap(self):
        print(self.heap)



if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(100)
    heap.insert(99)
    heap.insert(98)
    heap.insert(82)
    heap.insert(80)
    heap.insert(79)
    heap.insert(71)
    heap.print_heap()

    print("Max element:", heap.extract_max())
    heap.print_heap()


    print("Max element:", heap.get_max())