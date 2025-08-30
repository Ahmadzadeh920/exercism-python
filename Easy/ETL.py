'''Loop through the old dictionary.

For each letter in the list, create an entry in the new dictionary.

Convert the letter to lowercase.
'''

# Convert to new format: one-to-one mapping
def convert_to_one_to_one(old_format):
    new_format = {}
    for index, letter in old_format.items():
        for char in letter:
            new_format[char.lower()] = index
    return new_format


# Example Usage
if __name__ == "__main__":
    old_format = {
        1: "A B C",
        2: "D E F",
        3: "G H I",
        4: "J K L",
        5: "M N O",
        6: "P Q R S",
        7: "T U V",
        8: "W X Y Z"
    }
    new_format = convert_to_one_to_one(old_format)
    print(new_format)