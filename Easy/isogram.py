
def is_isogram(phrase:str)-> bool:
    """
    Determine if a word or phrase is an isogram.
    
    An isogram has no repeating letters (case-insensitive), 
    but spaces and hyphens are allowed to occur multiple times.
    
    Args:
        phrase (str): The word or phrase to check.
        
    Returns:
        bool: True if the phrase is an isogram, False otherwise.
    """

    normalized = phrase.lower()
    seen_char =set()
    for char in phrase:
        if not char.isalpha():
            continue
        if char in seen_char:
            return False
        seen_char.add(char)

    return True



#Example usega

if __name__ == "__main__":
     test_cases = [
        "lumberjacks",
        "background",
        "downstream",
        "six-year-old",
        "isograms"]
    for test in test_cases:
        print(f"{test}:{is_isogram(test)}")