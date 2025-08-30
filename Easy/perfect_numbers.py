def classify(number: int) -> str:
    """
    Classify a positive integer as 'perfect', 'abundant', or 'deficient'
    based on Nicomachus' classification scheme.
    
    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if number<1:
        raise ValueError("the number must be positive and higher that 0")
    
    
    divisors = [i for i in range(1, number) if number % i == 0]

    sum_of_divisors = sum(divisors)
    if sum_of_divisors == number:
        return "perfect"
    elif sum_of_divisors > number:
        return "abundant"
    else:
        return "deficient"


# Example usage
if __name__ == "__main__":
    test_cases = [6, 12, 8, 28, 15]
    for num in test_cases:
        print(f"The number {num} is classified as {classify(num)}")
        


