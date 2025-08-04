def has_duplicates(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Example usage:
if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 4]))  # Output: False
    print(has_duplicates([1, 2, 3, 4, 2]))  # Output: True