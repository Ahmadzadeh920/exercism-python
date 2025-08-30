def rotational_cipher(text:str,key:int)-> str:
    """
    Encrypts the input text using a rotational (Caesar) cipher.
    
    Parameters:
    text (str): The input string to encrypt.
    key (int): The shift value (0-26) for the cipher.
    
    Returns:
    str: The encrypted text.
    """

    result = ""

    for char in text:
        if  char.isupper():
            shifted = ord(char)-ord('A') + key
            wrapped = shifted % 26
            new_char = chr(wrapped + ord('A'))
            result += new_char
        elif char.islower():
            shifted = ord(char)-ord('a') + key
            wrapped = shifted % 26
            new_char = chr(wrapped + ord('a'))
            result += new_char
        else:
            result += char      

    return result


# Example usage
if __name__ == "__main__":
    test_cases = [
        ("Hello, World!", 3),
        ("abcXYZ", 2),
        ("Python 3.8", 5),
        ("Rotate Me!", 13)
    ]
    
    for text, key in test_cases:
        encrypted = rotational_cipher(text, key)
        print(f"Original: '{text}' | Key: {key} | Encrypted: '{encrypted}'")