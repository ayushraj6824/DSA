
def reverse1_word(s):
    words = s.split()
    reversed_words = []
    for i in range(len(words)-1, -1, -1):
        reversed_words.append(words[i])
    return ' '.join(reversed_words)

    



s="hello how are you"
print(reverse1_word(s))
