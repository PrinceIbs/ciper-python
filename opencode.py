def deciper(cipherText, key):

    deciperText = ''
    lower, upper = [], []

    for i in range(65, 91):
        upper.append(chr(i))
        lower.append(chr(i + 32))

    for char in cipherText:
        if char.isalpha():
            if char.isupper():
                index_of_char = upper.index(char) - key
                if index_of_char < 0:
                    new_index = len(upper) + index_of_char
                    deciperText += upper[new_index]
                else:
                    deciperText += upper[index_of_char]
            elif char.islower():
                index_of_char = lower.index(char) - key
                if index_of_char < 0:
                    new_index = len(lower) + index_of_char
                    deciperText += lower[new_index]
                else:
                    deciperText += lower[index_of_char]
        else:
            deciperText += char


    return deciperText
