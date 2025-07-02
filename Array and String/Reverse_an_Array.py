# Reverse an Array
def reverse_array(arr):
    if not arr:
        return []  

    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])  
    return reversed_arr


# Example usage
arr1=[1,2,3,4,5]
print(reverse_array(arr1))  # Output: [5, 4, 3, 2, 1]
# Example usage with an empty array
arr2 = []   
print(reverse_array(arr2))  # Output: []
# Example usage with a single element array 
arr3 = [42]
print(reverse_array(arr3))  # Output: [42]