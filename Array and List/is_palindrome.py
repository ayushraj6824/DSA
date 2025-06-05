def is_palindrome(arr):

    return arr == arr[::-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1]            
    palindrome = is_palindrome(arr)                    
    print(f"Is the array a palindrome? {palindrome}")