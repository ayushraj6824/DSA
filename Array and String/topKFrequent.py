def topKFrequent(nums, k):
    from collections import Counter
    
    # Count the frequency of each number in nums
    count = Counter(nums)
    
    # Get the k most common elements
    most_common = count.most_common(k)
    
    # Extract just the elements from the tuples returned by most_common
    return [num for num, freq in most_common]

# Example usage:
if __name__ == "__main__":  
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))  # Output: [1, 2]  
