def topKFrequent(nums, k):
    from collections import Counter
    import heapq

    # Count the frequency of each number
    count = Counter(nums)
    
    # Use a heap to find the k most frequent elements
    return heapq.nlargest(k, count.keys(), key=count.get)