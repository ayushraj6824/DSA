def rotate_array(arr, k):
    """
    Rotates the array to the right by k steps.
    
    :param arr: List of integers to be rotated
    :param k: Number of steps to rotate the array
    :return: Rotated list
    """
    n = len(arr)
    if n == 0:
        return arr
    k = k % n  # Handle cases where k is greater than n
    return arr[-k:] + arr[:-k]


# Example usage:
    arr = [1, 2, 3, 4, 5]                               
    k = 2                                                                                                       
    rotated_arr = rotate_array(arr, k)      
    print(rotated_arr)  # Output: [4, 5, 1, 2, 3]       

