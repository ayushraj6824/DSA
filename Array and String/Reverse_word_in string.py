
def reverse1_word(s):

    # Using split and join to reverse the words in the string
    return ' '.join(s.split()[::-1])    
    # return ' '.join(s.split()[::-1])



s="hello how are you"
print(reverse1_word(s))
