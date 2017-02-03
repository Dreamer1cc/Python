def anti_vowel(string):
    new_string = ''
    for a in string:
        if a in "aeiouAEIOU":
            new_string += '' 
        else:
            new_string += a
    return new_string