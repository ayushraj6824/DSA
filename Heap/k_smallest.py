# k smallest in heap
# Time complexity: O(k log n)   
# Space complexity: O(n)
import heapq

def k_smallest_elements(arr, k):
    if k <= 0 or k > len(arr):
        return []

    # Create a max heap with the first k elements
    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)

    # Process the remaining elements
    for num in arr[k:]:
        if -num > max_heap[0]:  # Compare with the max element
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    # Return the k smallest elements (negated back to positive)
    return [-x for x in max_heap]

# Example usage 
if __name__ == "__main__":
    arr = [3, 1, 5, 12, 2, 11, 4]
    k = 3
    print(k_smallest_elements(arr, k))  # Output: [1, 2, 3]





 
