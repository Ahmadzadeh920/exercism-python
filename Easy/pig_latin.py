'''
Split the sentence into words.

For each word, check rules in order:

Rule 1: vowel or xr, yt

Rule 3: consonants + qu

Rule 4: consonants + y

Rule 2: consonants only

Transform the word according to the rule.

Join the words back into a sentence.
'''

def pig_latin(word:str)->str:
    vowels = "aeiou"
      # Rule 1: Starts with vowel or 'xr', 'yt'
    if word[0] in vowels or word.startswith(("xr", "yt")):
        return word + "ay"

    # Rule 3: Starts with consonants followed by 'qu'
    # Find leading consonants
    index = 0
    while index < len(word) and word[index] not in vowels:
        if word[index:index+2] == "qu":
            index += 2
            break
        index += 1
    if index > 0:
        return word[index:] + word[:index] + "ay"
    
    # Rule 2 & 4: Starts with consonants or consonants followed by 'y'
    # Find first vowel or 'y'
    index = 0
    while index < len(word) and word[index] not in vowels + "y":
        index += 1
    return word[index:] + word[:index] + "ay"



def translate(sentence):
    """
    Translate a full sentence to Pig Latin.
    """
    words = sentence.split()
    return " ".join(pig_latin(word) for word in words)



# Example Usage
examples = [
    "apple", "xray", "yttria",
    "pig", "chair", "thrush",
    "quick", "square",
    "my", "rhythm"
]

for word in examples:
    print(f"{word} -> {pig_latin(word)}")

# Sentence example
sentence = "quick brown fox"
print("\nSentence:")
print(translate(sentence))  # "ickquay ownbray oxfay"












def translate(sentence):
    """
    Translate a full sentence to Pig Latin.
    """
    words = sentence.Split()
    return " " .join(pig_latin(word) for word in words)