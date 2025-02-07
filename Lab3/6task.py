def reverse_word(s):
    words = s.split()  
    reversed_s = " ".join(reversed(words))  
    return reversed_s  

hirako = input(" ")  
print(reverse_word(hirako))