def find_duplicate(arr):
    
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None 



  
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 3,2]            
    duplicate = find_duplicate(arr)                    
    print(f"Duplicate element: {duplicate}")  

