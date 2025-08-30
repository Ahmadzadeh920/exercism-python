'''
Takes an optional name as input.

'''

def two_fer(name="you"):
    """
    Return a two-fer string with the given name.

    Args:
        name (str, optional): The name to include in the two-fer. Defaults to "you".

    Returns:
        str: A formatted two-fer string.
    """
    return f"One for {name}, one for me."


#Example Usage
if __name__ == "__main__":
    print(two_fer())  # Output: "One for you, one for me."
    print(two_fer("Alice"))  # Output: "One for Alice, one for me."
    print(two_fer("Bob"))  # Output: "One for Bob, one for me."