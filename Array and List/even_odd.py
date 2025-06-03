def count_even_odd(numbers):

    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    even_count, odd_count = count_even_odd(numbers)
    print(f"Even count: {even_count}, Odd count: {odd_count}")