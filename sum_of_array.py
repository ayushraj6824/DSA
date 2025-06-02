def sum_of_array(arr):
    sum=0
    for i in arr:
        sum+=i  
    return sum


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    result = sum_of_array(arr)
    print(f"The sum of the array is: {result}")