# List of tuples: (noun phrase, verb phrase)
# Each element represents the new addition for that verse
story_elements = [
    ("the house that Jack built.", ""),  # base case has no verb
    ("the malt", "lay in"),
    ("the rat", "ate"),
    ("the cat", "killed"),
    ("the dog", "worried"),
    ("the cow with the crumpled horn", "tossed"),
    ("the maiden all forlorn", "milked"),
    ("the man all tattered and torn", "kissed"),
    ("the priest all shaven and shorn", "married"),
    ("the rooster that crowed in the morn", "woke"),
    ("the farmer sowing his corn", "kept"),
    ("the horse and the hound and the horn", "belonged to")
]

def build_verse(n: int) -> str:
    """
    Build the nth verse of 'The House That Jack Built' recursively.
    
    Args:
        n (int): The index of the verse (0-based).
    
    Returns:
        str: Full verse as a string.
    """
    verse_lines = [f"This is {story_elements[n][0]}"]
    
    # Add all previous story elements in reverse order
    for i in range(n, 0, -1):
        verb = story_elements[i][1]
        obj = story_elements[i-1][0]
        verse_lines.append(f"that {verb} {obj}")
    
    return "\n".join(verse_lines)

def recite_rhyme() -> str:
    """
    Generate the full nursery rhyme.
    
    Returns:
        str: Full rhyme as a string.
    """
    full_rhyme = []
    for i in range(len(story_elements)):
        full_rhyme.append(build_verse(i))
        full_rhyme.append("")  # empty line between verses
    return "\n".join(full_rhyme)

# ---- Example Usage ----
print(recite_rhyme())
