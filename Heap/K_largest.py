# kth leargest element in an array using heapq
# Time complexity: O(k log n)   
# Space complexity: O(n)
import heapq
def k_largest_elements(arr, k):
    if k <= 0 or k > len(arr):
        return []

    # Create a min heap with the first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # Process the remaining elements
    for num in arr[k:]:
        if num > min_heap[0]:  # Compare with the min element
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # Return the k largest elements
    return min_heap
# Example usage
if __name__ == "__main__":  
    arr = [3, 1, 5, 12, 2, 11, 4]
    k = 3
    print(k_largest_elements(arr, k))  # Output: [5, 12, 11]