# Program to find the occurences of alphabets in a given string.

def alpha_counter(s:str):
    alpha_dict = {}
    for letter in s.lower():
        if letter in alpha_dict:
            alpha_dict[letter] += 1
        else:
            alpha_dict[letter] = 1
    
    return alpha_dict

