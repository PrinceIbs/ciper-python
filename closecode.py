            
def ciper(text, key):
    
    cipher = ''
    text = text
    
    # create a list of lower and upper alphabet
    lower = []
    upper = []
    for i in range(65, 91):
        upper.append(chr(i))
        lower.append(chr(i+32))

    for char in text:
        # engine of algorithm
        if char.isalpha():
            if char.isupper():
                # locate the character
                index_of_char = upper.index(char) + key
                if index_of_char > len(upper) - 1:
                    new_index = index_of_char - len(upper)
                    # adds the new letter to the encoded string
                    cipher += upper[new_index]
                else:
                    cipher += upper[index_of_char]
            elif char.islower():
                # handles lowercase
                index_of_char = lower.index(char) + key
                if index_of_char > len(lower) - 1:
                    new_index = index_of_char - len(lower)
                    cipher += lower[new_index]
                else:
                    cipher += lower[index_of_char]
        else:
            cipher += char

    return cipher


