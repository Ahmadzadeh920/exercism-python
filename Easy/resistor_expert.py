# Digit color mapping (for value & multiplier)
digit_colors = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

# Tolerance color mapping
tolerance_colors = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}

def resistor_label(bands: list) -> str:
    """
    Translate resistor color bands (1, 4, or 5 bands) into human-readable resistance.

    Args:
        bands (list): List of band colors.

    Returns:
        str: Human-readable resistance value with tolerance (e.g., "33 ohms ±0.5%").
    """


    bands = [band.lower() for band in bands]

    # Case 1: One band resistor
    if len(bands) == 1 and bands[0] == "black":
        return "0 ohms"
    elif not 3<len(bands)<6:
        raise ValueError("the lenght of bands must be 4 or 5")
    elif len(bands)==4:
        value1 = digit_colors.index(bands[0])
        value2 = digit_colors.index(bands[1])
        multiplier = (10**int(digit_colors.index(bands[2])))
        tolerance = tolerance_colors[bands[3]]
        resistance = (int(f"{value1}{value2}")*multiplier)
    elif len(bands)==5:
        value1 = digit_colors.index(bands[0])
        value2 = digit_colors.index(bands[1])
        value3 = digit_colors.index(bands[2])
        multiplier = (10**int(digit_colors.index(bands[3])))
        tolerance = tolerance_colors[bands[4]]
        resistance = (int(f"{value1}{value2}{value3}")*multiplier)



    # Determine the unit
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

    return f"{value} {unit} {tolerance}"


# Example Usage
if __name__=="__main__":
    test_cases = [["orange", "orange", "black", "green"],["orange", "orange", "orange", "black", "green"],["black"]]
    for test in test_cases:
        print(f"for this {test} the value is {resistor_label(test)}")