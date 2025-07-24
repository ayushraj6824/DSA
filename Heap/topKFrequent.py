def topKFrequent(nums, k):
    from collections import Counter
    import heapq

    # Count the frequency of each number
    count = Counter(nums)
    
    # Use a heap to find the k most frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)





# Example usage:
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))    


