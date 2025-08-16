def minEatingSpeed(piles, h):
    def canEatAll(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Equivalent to math.ceil(pile / speed)
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if canEatAll(mid):
            right = mid
        else:
            left = mid + 1
    return left 

# Example usage:
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4