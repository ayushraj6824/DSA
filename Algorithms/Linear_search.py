def linear_search(arr, target):
  
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1



# Example usage:
arr=[1, 2, 3, 4, 5]
target = 3  
result = linear_search(arr, target)
print("Element found at index:", result if result != -1 else "Not Found")   

#example usage with a target not in the array
target_not_found = 6        
result_not_found = linear_search(arr, target_not_found)
print("Element found at index:", result_not_found if result_not_found != -1 else "Not Found")   
