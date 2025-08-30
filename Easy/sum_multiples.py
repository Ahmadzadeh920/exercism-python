'''Input:

level → the level number the player finished.

factors → list of magical item base values.

Process:

For each factor, generate all multiples of that factor that are less than level.

Combine all multiples into a set (so duplicates like 15 from both 3 and 5 aren’t counted twice).

Sum all unique multiples.

Output:

Total energy points (int).'''


def sum_multiples(level: int, factors: list) -> int:
    """
    Calculate the sum of all unique multiples of given factors below a certain level.

    Args:
        level (int): The level number the player finished.
        factors (list): List of magical item base values.

    Returns:
        int: Total energy points.
    """
    multiples = set()
    
    for factor in factors:
        if factor == 0:
            continue
        for multiple in range(factor, level, factor):
            multiples.add(multiple)
    
    return sum(multiples)


#Example Usage
if __name__ == "__main__":
    level = 20
    factors = [3, 5]
    print(sum_multiples(level, factors))  # Output: 78
    level = 100
    factors = [3, 5, 7]
    print(sum_multiples(level, factors))  # Output: 2738
    