def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # mid= left + (right - left) // 2
        mid = left + (right - left) // 2    
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


# Example usage:
arr = [ 3 ]       
target = 3
result = binary_search(arr, target) 
print("Element found at index:", result if result != -1 else "Not Found")

 
