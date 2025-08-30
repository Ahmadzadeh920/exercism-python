# Define resistor colors
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


def resistor_value(color1: str, color2: str, color3: str) -> str:
    """
    Given three resistor colors, return the resistance value with units.

    Args:
        color1 (str): First band color
        color2 (str): Second band color
        color3 (str): Multiplier band color

    Returns:
        str: Resistance value (e.g., "33 ohms", "3300 ohms", "33 kiloohms").
    """

    c1, c2, c3 = color1.lower() , color2.lower() , color3.lower()
    first_digit = resistor_colors.index(c1)
    second_digit = resistor_colors.index(c2)
    multiplier = resistor_colors.index(c3)
    digits = int(f"{first_digit}{second_digit}")
    resistance = digits *(10** multiplier)
    # Choose correct unit (ohms, kiloohms, megaohms, gigaohms)
    if resistance >= 1_000_000_000:
        value = resistance // 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        value = resistance // 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance // 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    return f"{value} {unit}"


#Example Usage
if __name__=="__main__":
    test_cases = [["orange", "orange", "black"],["orange", "orange", "red"],["orange", "orange", "orange"]]
    for test in test_cases:
        print (f"the trio resistor for this list {test} is {resistor_value(test[0], test[1], test[2])}")

