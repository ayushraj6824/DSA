def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = ''.join(sorted(s))
        anagrams.setdefault(key, []).append(s)
    return list(anagrams.values())
# Example usage:
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]    