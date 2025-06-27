def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


# Example usage:
arr = [1, 2, 3, 4, 5]       
target = 3
result = binary_search(arr, target) 
print("Element found at index:", result if result != -1 else "Not Found")

# Example usage with a target not in the array
target_not_found = 6    
result_not_found = binary_search(arr, target_not_found)
print("Element found at index:", result_not_found if result_not_found != -1 else "Not Found")
# Example usage with an empty array
empty_arr = []  
result_empty = binary_search(empty_arr, target)
print("Element found at index:", result_empty if result_empty != -1 else "Not Found")   
