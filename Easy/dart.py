import math

def score(x, y):
    """
    Calculate the score of a single dart throw based on its coordinates (x, y).
    
    The dartboard has three concentric circles centered at (0, 0):
    - Inner circle: radius 1 → 10 points
    - Middle circle: radius 5 → 5 points
    - Outer circle: radius 10 → 1 point
    - Outside outer circle: radius > 10 → 0 points
    """
    distance = math.sqrt(x**2 + y**2)
    
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0


# Example usage
if __name__ == "__main__":
    test_cases = [(0, 0), (3, 4), (6, 8), (11, 0)]
    for x, y in test_cases:
        print(f"For coordinates ({x}, {y}), the score is {score(x, y)}")