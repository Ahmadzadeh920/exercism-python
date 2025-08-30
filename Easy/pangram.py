import string

def is_pangram(sentence: str) -> bool:
    """
    Return True if `sentence` uses every letter a–z at least once (case-insensitive),
    ignoring digits, punctuation, and other symbols. Otherwise, return False.
    """
    # Set of all English lowercase letters
    ALPHABET = set(string.ascii_lowercase)

    # Normalize sentence to lowercase
    sentence = sentence.lower()

    # Keep only alphabetic characters
    letters_in_sentence = {char for char in sentence if char.isalpha()}

    # Keep only letters from English alphabet (ignore accents etc.)
    letters_in_sentence = letters_in_sentence.intersection(ALPHABET)

    # Check if the sentence contains all letters
    return letters_in_sentence == ALPHABET


# ---- Quick self-checks / examples ----
if __name__ == "__main__":
    tests = [
        ("The quick brown fox jumps over the lazy dog.", True),
        ("Sphinx of black quartz, judge my vow!", True),
        ("Pack my box with five dozen liquor jugs.", True),
        ("Hello, world!", False),
        ("", False),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),  # uppercase only still counts
        ("1234 !@#$%^&*()", False),
    ]

    for text, expected in tests:
        got = is_pangram(text)
        print(f"{got == expected:5} | expected={expected:5} | got={got:5} | {text}")
