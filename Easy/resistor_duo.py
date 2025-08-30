'''
Each color maps to a digit.

The first 2 bands form a two-digit number.

Example:

brown (1) + green (5) → 15

brown (1) + green (5) + violet (7) → still 15 (ignore extra colors).


'''

# Define the resistor color code as a list
resistor_colors = [
    "black",  # 0
    "brown",  # 1
    "red",    # 2
    "orange", # 3
    "yellow", # 4
    "green",  # 5
    "blue",   # 6
    "violet", # 7
    "grey",   # 8
    "white"   # 9
]


def value(colors: list) -> int:
    if (len(colors)<2):
        raise ValueError("the length of the list must be at minimum 2")
    colors = [color.lower() for color in colors]
    first_digit = resistor_colors.index(colors[0])
    second_digit = resistor_colors.index(colors[1])
    value = int(f"{first_digit}{second_digit}")
    return value

# Example Usage
if __name__ =="__main__":
    test_cases = [["yellow", "white"], ["brown", "red", "black"]]
    for test in test_cases:
        print(f"the valus of this {test} is {value(test)}")