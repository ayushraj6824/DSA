def merge_k_sorted_arrays(arrays):
    import heapq

    # Create a min heap
    min_heap = []
    
    # Initialize the heap with the first element of each array
    for i, array in enumerate(arrays):
        if array:  # Check if the array is not empty
            heapq.heappush(min_heap, (array[0], i, 0))  # (value, array index, element index)

    merged_array = []

    while min_heap:
        value, arr_index, elem_index = heapq.heappop(min_heap)
        merged_array.append(value)

        # If there is a next element in the same array, add it to the heap
        if elem_index + 1 < len(arrays[arr_index]):
            next_value = arrays[arr_index][elem_index + 1]
            heapq.heappush(min_heap, (next_value, arr_index, elem_index + 1))

    return merged_array

# example usage
if __name__ == "__main__":  
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(merge_k_sorted_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]