def reverse_string(string:str)-> str:
    """
    Reverse a given string and return the result.
    
    Args:
        text (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    # Using Python slicing [::-1]
    # - [start:end:step]
    # - Leaving start and end blank means "use the whole string"
    # - step = -1 means "read backwards"
    return string[::-1]


# Example usage
if __name__ == "__main__":
    test_cases = ["hello", "world", "Python", "reverse"]
    for text in test_cases:
        print(f"The reverse of '{text}' is '{reverse_string(text)}'")
