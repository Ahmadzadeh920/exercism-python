"""
    Generates the Collatz sequence starting from a positive integer n.
    
    Rules:
    - If n is even, divide it by 2.
    - If n is odd, multiply it by 3 and add 1.
    - Repeat until n becomes 1.
    
    Returns:
        sequence (list): A list containing the Collatz sequence starting from n.
        steps (int): Number of steps taken to reach 1 (excluding the starting number).
    """

def collatz_sequence(n):
    
    if n<2:
        raise ValueError("the number must be highr than 1")
    sequence = [n]

    while n != 1:
        if n%2==0:
            n = n//2
            sequence.append(n)
        else:
            n = n*3+1
            sequence.append(n)

    total_step = len(sequence)-1
    print(f"for this {n} as digit , {total_step} is running includes{sequence}")



# Example Usage
if __name__ == "__main__":
    test = 12
    collatz_sequence(test)




