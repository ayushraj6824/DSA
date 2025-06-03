def second_largest_element(arr):
    if not  arr:
        return None
    
    largest=arr[0]
    slargest=-1

    for i in arr:
        if arr[i]> largest:
            slargest=largest
            largest=arr[i]
        else:
            if arr[i] < largest and arr[i] > slargest:
                slargest = arr[i]
    return slargest

# Example usage
if __name__ == "__main__":
    example_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    second_largest = second_largest_element(example_array)
    print(f"The second largest element in the array is: {second_largest}")