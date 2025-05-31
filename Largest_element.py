# Find the Largest Element in an Array
def find_largest_element(arr):
    if not arr:
        return None  # Return None if the array is empty

    largest = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > largest:
            largest = num  # Update largest if a larger number is found
    return largest

# Example usage
if __name__ == "__main__":
    example_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    largest_element = find_largest_element(example_array)
    print(f"The largest element in the array is: {largest_element}")    