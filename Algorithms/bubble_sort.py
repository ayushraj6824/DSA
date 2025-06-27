def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(unsorted_array)
print("Sorted array is:", sorted_array) 
# Example usage with an already sorted array
already_sorted_array = [11, 12, 22, 25, 34, 64, 90]
sorted_already_sorted = bubble_sort(already_sorted_array)
print("Sorted array is:", sorted_already_sorted)